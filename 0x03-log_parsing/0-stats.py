#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    # Define regular expression patterns for each section of the log entry
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    # Initialize dictionary to store extracted information
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    # Construct the log format using the defined patterns
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    # Use regular expression to match the log entry format
    resp_match = re.fullmatch(log_fmt, input_line)
    # If a match is found, extract status code and file size
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    # Extract information from the log entry
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    # Update the status code statistics
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    # Update the total file size
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    # Initialize dictionary to store statistics for each status code
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            # Update metrics for each log entry
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            # Print statistics every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Handle keyboard interrupt or end of file
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
