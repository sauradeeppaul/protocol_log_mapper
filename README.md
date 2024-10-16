# protocol_log_mapper
Parses a file containing flow log data and maps each row to a tag based on a lookup table

### Sources used:
- Sourcing the protocol mappings from: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
- Sourcing flow log formatting details from: https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-default

## Files required
- CSV for Lookup Table: `lookup_table.csv`
- CSV for Protocol Numbers: `protocol-numbers-1.csv`
- Text file for logs: `flow_logs.txt`

## Steps
- Run on python3 using `python3 parser`

## Assumptions
- Supports Default log format version 2
- Deprecated protocols are disregarded.
- Logs not following the mapping will be skipped.