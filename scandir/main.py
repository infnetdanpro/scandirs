import os
from time import time
from tools.path import scan_dir
from tools.csvlib import save_to_csv
from tools.custom_args import create_custom_args


def main():
    args = create_custom_args()
    print(f'Scanning directory: {args.dest}')
    files = scan_dir(args.dest)
    current_dir = os.getcwd()
    csv_filepath = os.path.join(current_dir, f'Report_scandirs_{int(time())}.csv')
    result = save_to_csv(files, csv_filepath)
    if not result:
        raise Exception('Error while saving results')

    print(csv_filepath)
    print('Rows:', len(files))


if __name__ == '__main__':
    main()
