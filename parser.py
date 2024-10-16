import csv
from collections import defaultdict

protocol_mapping = {}
lookup_dict = {}
tag_counts = defaultdict(int)
port_protocol_counts = defaultdict(int)

def load_protocol_mappings():
	with open('protocol-numbers-1.csv', 'r', newline='') as protocol_file:
	    reader = csv.DictReader(protocol_file)
	    for row in reader:
	        decimal = row['Decimal'].strip()
	        keyword = row['Keyword'].strip().lower()

	        # Leave out the deprecated tags
	        if 'deprecated' not in keyword:
	            protocol_mapping[decimal] = keyword

def load_lookup_table():
	with open('lookup_table.csv', 'r') as lookup_file:
	    reader = csv.DictReader(lookup_file)
	    for row in reader:
	        dstport = row['dstport'].strip()
	        protocol = row['protocol'].strip().lower()
	        tag = row['tag'].strip()

	        key = (dstport, protocol)
	        lookup_dict[key] = tag


def parse_flow_logs():
	with open('flow_logs.txt', 'r') as flow_log_file:
	    for line in flow_log_file:
	        fields = line.strip().split()
	        # Skip incomplete lines
	        if len(fields) < 14:
	            continue

	        dstport = fields[6].strip()
	        protocol_number = fields[7].strip()

	        protocol_name = protocol_mapping.get(protocol_number, 'unknown')

	        protocol_name = protocol_name.lower()
	        key = (dstport, protocol_name)

	        tag = lookup_dict.get(key, 'Untagged')

	        tag_counts[tag] += 1
	        port_protocol_counts[key] += 1


load_protocol_mappings()
load_lookup_table()
parse_flow_logs()

with open('output.txt', 'w') as output_file:
    output_file.write('Tag Counts:\n')
    output_file.write('Tag,Count\n')
    for tag, count in tag_counts.items():
        output_file.write(f'{tag},{count}\n')

    output_file.write('\nPort/Protocol Combination Counts:\n')
    output_file.write('Port,Protocol,Count\n')
    for (port, protocol), count in port_protocol_counts.items():
        output_file.write(f'{port},{protocol},{count}\n')