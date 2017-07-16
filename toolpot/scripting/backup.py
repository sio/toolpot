"""
Tools for writing backup scripts
"""


import os
import tarfile
from datetime import datetime
from glob import glob


def archive(archive_file, *content):
    """Create tar.gz archive, do not repeat unnecessary directory structure"""
    if len(content):
        archive_dir = os.path.dirname(archive_file)
        if archive_dir and not os.path.isdir(archive_dir):
            raise ValueError("directory not found: %s" % archive_dir)
        base_dir = common_parent(*content)
        with tarfile.open(archive_file, "w:gz") as tar:
            for path in content:
                kwargs = dict()
                if base_dir:
                    arc_path = os.path.relpath(path, base_dir)
                    if arc_path == ".":
                        arc_path = os.path.basename(path)
                    kwargs["arcname"] = arc_path
                try:
                    tar.add(path, **kwargs)
                except FileNotFoundError:
                    print("Path not found, skipping: %s" % path)
        print("Created archive: %s" % archive_file)


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


def make_name(prefix="", date_format="%Y%m%d-%H%M", extension="tar.gz"):
    """Generate archive name that can be used for sorting (prefix_date.extension)"""
    parts = list()
    if prefix: parts.append(prefix)
    parts.append(datetime.now().strftime(date_format))
    return "_".join(parts) + "." + extension


def list_backups(directory, prefix=""):
    """Find previously made backups"""
    pattern = os.path.join(directory, prefix + "*")
    return glob(pattern)


def rotate(directory, prefix="", max_number=10):
    """
    Remove old backups or logs

    Older files MUST come first when sorted by filename
    """
    files = sorted(list_backups(directory, prefix))
    deleted_count = 0
    while len(files) > max_number:
        os.remove(files.pop(0))
        deleted_count += 1
    if deleted_count: print("Deleted %s old file(s)" % deleted_count)
