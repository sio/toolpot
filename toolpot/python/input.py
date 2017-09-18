"""
Parse user input
"""


import re
from collections import defaultdict
from datetime import timedelta


def parse_time(interval):
    """
    Parse time intervals like the ones given to Linux sleep command:
    NUMBER[SUFFIX]

    Example: '3m'    = 3 minutes
             '5h 1m' = 5 hours 1 minutes
             '21'    = 21 seconds

    SUFFIX may be 's' for seconds (the default), 'm' for minutes, 'h' for
    hours 'd' for days or 'w' for weeks.  NUMBER has to be an integer.
    Given two or more whitespace separated words, return the amount of time
    specified by the sum of their values.

    Return datetime timedelta object.
    """
    expanded = {"w": "weeks",
                "d": "days",
                "h": "hours",
                "m": "minutes",
                "s": "seconds",
                "" : "seconds"}
    pattern = re.compile(r"\s*(\d+)([wdhms]?)\s*")

    parsed = defaultdict(int)
    for word in str(interval).split():
        match = pattern.match(word)
        if match:
            number, suffix = match.groups()
            parsed[expanded[suffix]] += int(number)
        else:
            message = "invalid time interval: {}".format(word)
            raise ValueError(message)
    return timedelta(**parsed)
