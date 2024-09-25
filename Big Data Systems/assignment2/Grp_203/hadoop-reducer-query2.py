#!/usr/bin/python3
import sys
import logging

logger = logging.getLogger(__name__)


def reducer():
    current_year = '2010'
    total_quantity = 0
    logging.basicConfig(filename='/home/anirudh/hadoop-3.3.2/logs/python_logs/reduce.log', level=logging.INFO)
    previous_stock_code = None
    # Input comes from STDIN
    for line in sys.stdin:

        stock_code, date, quantity = line.strip().split('\t')

        if current_year in date:
            if (previous_stock_code == None):
                previous_stock_code = stock_code

            if (previous_stock_code != stock_code):
                print(f"{previous_stock_code}\t{total_quantity}")
                previous_stock_code = stock_code
                total_quantity = 0

            quantity = int(quantity)
            total_quantity += quantity
        else: logger.error('{}'.format(date))

    # # Emit the last key-value pair
    # print(f"{stock_code}\t{date}\t{quantity}")

if __name__ == "__main__":
    reducer()
