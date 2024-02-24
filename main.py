import csv
import os
from config import *

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = [field for field in reader.fieldnames if config.get(field, False)]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if all(row[key] for key, value in config.items() if value):
                if phone_filter_include != []:
                    if any(row.get('phone', '').startswith(prefix) for prefix in phone_filter_include):
                        filtered_row = {key: value for key, value in row.items() if key in fieldnames}
                        writer.writerow(filtered_row)
                elif phone_filter_exclude != []:
                    if not any(row.get('phone', '').startswith(prefix) for prefix in phone_filter_exclude):
                        filtered_row = {key: value for key, value in row.items() if key in fieldnames}
                        writer.writerow(filtered_row)
                else:
                    filtered_row = {key: value for key, value in row.items() if key in fieldnames}
                    writer.writerow(filtered_row)

def process_folder(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(input_directory):
        if file_name.endswith('.csv'):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_path = os.path.join(output_directory, file_name)
            process_csv(input_file_path, output_file_path)

process_folder(input_folder, output_folder)
