#!/usr/bin/python3
"""
Log Parsing
"""

import sys
stcd = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
summ = 0


def prn_stats():
    """
    Function that prints stats about a log
    """
    global summ

    print('File size: {}'.format(summ))
    stcdor = sorted(stcd.keys())
    for each in stcdor:
        if stcd[each] > 0:
            print('{}: {}'.format(each, stcd[each]))


if __name__ == "__main__":
    cnt = 0
    try:
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                if fact[-2] in stcd:
                    stcd[fact[-2]] += 1
                summ += int(fact[-1])
            except Exception as e:
                pass
            cnt += 1
            if cnt == 10:
                prn_stats()
                cnt = 0
    except KeyboardInterrupt:
        prn_stats()
        raise
    else:
        prn_stats()
