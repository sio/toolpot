"""
Find and delete duplicated files
"""

import os
from collections import defaultdict, namedtuple

from .fileops import file_hash


def find_duplicates(paths):
    """
    Find duplicate files in given sequence of paths.

    Return a dictionary where keys contain duplicate metadata (size, hash)
    and values are lists of filepaths that have this metadata in common

    Sample output:
    >> find_duplicates(["/path/to/foo", "/path/to/foo2", "/path/to/bar"])
    {
        Duplicate(size=`foo_size`, hash=`foo_hash`):
            ["/path/to/foo", "/path/to/foo2"]
    }
    """
    if isinstance(paths, str):
        paths = [paths,]

    def traverse(directory):
        for parent, dirs, files in os.walk(directory):
            for filename in files:
                yield os.path.join(parent, filename)

    sizes = defaultdict(list)
    for item in paths:
        if os.path.isdir(item):
            files = traverse(item)
        else:
            files = [item]
        for name in files:
            sizes[os.path.getsize(name)].append(name)

    Duplicate = namedtuple("Duplicate", ["size", "hash"])
    hashes = defaultdict(list)
    for size, files in sizes.items():
        if len(files) > 1:
            for name in files:
                hash = file_hash(name)
                hashes[Duplicate(size, hash)].append(name)

    return {info: paths for info, paths in hashes.items() if len(paths)>1}


def remove_duplicates(paths, keep_new=False):
    """
    Given a sequence of paths to files find duplicates among them and
    delete all duplicated files keeping only the oldest one.

    If keep_new=True keeps the newest of duplicates.
    """
    for files in find_duplicates(paths).values():
        ordered = sorted(files, key=os.path.getctime, reverse=keep_new)
        while len(ordered) > 1:
            os.remove(ordered.pop())
