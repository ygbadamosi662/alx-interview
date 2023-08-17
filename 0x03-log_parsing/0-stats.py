#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""
import re
import sys


def increment(on_the_plus_side, x):
    """
    Defines function increment, increments on_the_plus_side by
    x.
    Args:
    on_the_plus_side: int
    x: int or str
    Return: int, sum of x and on_the_plus_side
    """
    return on_the_plus_side + int(x)


try:
    p = r'^[\d.]+ - \[[^\]]+\] "GET \/projects\/\d+ HTTP\/1\.1" \d{3} \d+$'
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    print_out = {'file_size': 0, 'status_codes': status_codes}
    i = 0
    j = 0

    def print_shit():
        """
        Defines function print_shit, prints the dict print_out
        in the below format:
        File Size: <total file_size>
        status code: code
        ...

        Return: does not return anything
        """
        print('File Size: {}'.format(print_out.get('file_size')))
        sorted_keys = sorted(print_out['status_codes'].keys())

        for key in sorted_keys:
            val = print_out['status_codes'].get(key)
            if val != 0:
                print('{}: {}'.format(key, val))

    for line in sys.stdin:
        j += 1
        if re.match(p, line):
            arr = line.split(' ')
            olodos = arr[-2:]
            status = olodos[0]
            file_size = olodos[1]
            print_out['file_size'] = increment(print_out.get('file_size'),
                                               file_size)

            if status.isdigit():
                pstatus = print_out['status_codes']
                pstatus[status] = increment(pstatus.get(status), 1)

        if (j - i) == 10:
            i = j
            print_shit()
except KeyboardInterrupt:
    print_shit()
