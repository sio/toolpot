"""
Common file and path operations
"""

import os.path
import hashlib


def common_parent(*paths, debug=False):
    """
    Find common parent directory of all given paths
    Keep in mind that this function does not implicitly resolve relative paths

    Standard library method os.path.commonprefix() does almost the same, but it
    will return "one/t" for ["one/two", "one/three"] which is not a valid path

    NOTE: Python 3.4 and 3.5 have usable standard library tools for this purpose
    """
    common = list()
    for element in zip(*(path_fullsplit(path) for path in paths)):
        if debug: print(element,)
        if all(e == element[0] for e in element):
            if debug: print("is common")
            common.append(element[0])
        else:
            if debug: print("different")
            break
    if common:
        return os.path.join(*common)
    else:
        return ""


def path_fullsplit(path):
    """Split path to a list of elements"""
    path = os.path.normpath(path)
    repeat_marker = False
    elements = list()
    while path:
        head, tail = os.path.split(path)
        if tail or not elements:
            elements.append(tail)
        if head == path:
            if repeat_marker:
                elements.append(head)
                break
            else:
                repeat_marker = True
        else:
            repeat_marker = False
        path = head
    elements.reverse()
    return elements
