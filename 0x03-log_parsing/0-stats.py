#!/usr/bin/python3
"""_summary_
    """
from sys import stdin
import re
import signal


valid = re.compile(
    '^[\d.]{0,15} - \[.+\] "GET /projects/260 HTTP/1.1" (200|301|400|401|403|404|405|500) (\d+)')
data = dict()
total_size = 0
i = 0


def CTRL_C(signum, frame):
    """_summary_

    Args:
        signum (_type_): _description_
        frame (_type_): _description_
    """
    print_data()
    global i
    i = 0


def print_data():
    """_summary_
    """
    print(f"File size: {total_size}")
    for k, v in sorted(data.items()):
        print(f"{k}: {v}")


signal.signal(signal.SIGINT, CTRL_C)


def parse():
    global data
    global i
    global total_size
    for line in stdin:
        res = valid.match(line)
        if res == None:
            continue

        status_code = int(res.groups()[0])
        file_size = int(res.groups()[1])
        total_size += file_size
        if status_code in data:
            data[status_code] += 1
        else:
            data[status_code] = 1
        i += 1
        if i == 10:
            print_data()
            i = 0


if __name__ == "__main__":
    parse()
