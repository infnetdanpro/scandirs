import csv
from typing import AnyStr, Union


def save_to_csv(files_sizes: AnyStr, csv_filename: AnyStr) -> Union[bool, None]:
    with open(csv_filename, 'w', encoding='utf-8-sig', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['#', 'filename', 'filesize', 'created', 'type'])
        i = 0
        for file_data in files_sizes:
            row = [i]
            for column in file_data:
                row.append(column)

            csv_writer.writerow(row)
            i += 1
        return True
    return
