from tools.path import scan_dir
from tools.csvlib import save_to_csv
import os
from time import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)


if __name__ == '__main__':
    files = scan_dir('D:\\Torrents\\')
    current_dir = os.getcwd()
    csv_filepath = os.path.join(current_dir, f'Report_scandirs_{int(time())}.csv')
    result = save_to_csv(files, csv_filepath)
    if not result:
        raise Exception('Error while saving results')
