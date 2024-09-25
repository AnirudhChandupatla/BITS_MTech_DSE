#!/usr/bin/python3
import sys
import logging

logger = logging.getLogger(__name__)


def reducer():
    current_year = '2010'
    total_revenue = 0
    logging.basicConfig(filename='/home/anirudh/hadoop-3.3.2/logs/python_logs/reduce.log', level=logging.INFO)
    # Input comes from STDIN
    for line in sys.stdin:
        #logger.info('{}'.format(line))
        # Split the input into key and value
        ##print(line)
        
        date, price = line.strip().split('\t')
        ##print('#',year,price)
        price = float(price)

        # Process key-value pairs
        if current_year in date:
            total_revenue += price
        else: logger.error('{}'.format(date))

    # Emit the last key-value pair
    print(f"{current_year}\t{total_revenue}")

if __name__ == "__main__":
    reducer()
