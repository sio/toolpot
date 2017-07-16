"""
An assorted collection of Python tools

You wouldn't expect a professional to store his tools in a clay pot, would you?
"""


__version__ = "0.0.1"
__author__ = "Vitaly Potyarkin"
__git__ = "git+git://github.com/sio/toolpot.git"


def update():
    """
    A shortcut for pip to update this package to the latest version in git repo

    This is intended to be used in the active development phase, please rely on
    pip as a recommended tool for day-to-day Python package management
    """
    import pip
    pip.main([
        "install",
        __git__,
        "--upgrade",
        "--no-deps",
        "--force-reinstall",
        "--ignore-installed"
        ])
