#!/usr/bin/python3
""" Module to print status code """
import sys

# Define variables to store metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    line_count = 0
    for line in sys.stdin:
        # Increment line count
        line_count += 1

        # Split the line by spaces
        parts = line.split()

        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # Print final statistics upon keyboard interruption
    print("Total file size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
