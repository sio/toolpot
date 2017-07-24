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
