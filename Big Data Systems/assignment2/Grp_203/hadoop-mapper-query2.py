#!/usr/bin/python3
import sys
import logging
import re
logger = logging.getLogger(__name__)
pattern = r'"([^"]*)"'
def replace_commas(match):
    return match.group(0).replace(",", "")

def mapper():
    logging.basicConfig(filename='/home/anirudh/hadoop-3.3.2/logs/python_logs/map.log', level=logging.INFO)
    # Input comes from STDIN (standard input)
    for line in sys.stdin:
        # Parse the CSV line
        try:
            line = re.sub(pattern, replace_commas, line)
            #logger.info('{}'.format(line))
            record = line.strip().split(',')
            if len(record) == 9:  # Ensure all columns are present
                stock_code = record[2]
                quantity = record[4]
                invoice_date = record[5]
                date = invoice_date.split()[0]
                # Emit key-value pair (year, price)
                print(f"{stock_code}\t{date}\t{quantity}")
            else: logger.error('{}'.format(line))
        except: logger.error('{}'.format(line))

if __name__ == "__main__":
    mapper()
