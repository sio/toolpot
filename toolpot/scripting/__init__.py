"""
Tools for day to day OS automation

Unix shell is an incredibly powerful tool and writing shell scripts can be
very fun, but Python offers ease of use and reuse far beyond what can be
found in shell. Plus Python smoothes a lot of edge cases
(read: string escaping) that can be time consuming to do properly in bash
"""

__all__ = [
    "archive",
    "make_name",
    "rotate",
    "common_parent",
    "file_hash",
    "find_duplicates",
    "remove_duplicates",
]

from .backup import archive, \
                    make_name, \
                    rotate
from .fileops import common_parent, \
                     file_hash
from .deduplicate import find_duplicates, \
                         remove_duplicates
