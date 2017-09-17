try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import toolpot

setup(
    name=toolpot.__name__,
    version=toolpot.__version__,
    description=toolpot.__doc__.strip().splitlines()[0],
    long_description=toolpot.__doc__.strip(),
    url="https://github.com/sio/toolpot",
    author=toolpot.__author__,
    author_email="sio.wtf@gmail.com",
    license="GPL-3.0",
    platforms="any",
    packages=[
        "toolpot", 
        "toolpot.scripting", 
        "toolpot.python", 
        "toolpot.sap", 
        "toolpot.linux",
        ],
    scripts=[],
    package_data={},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.3",
    zip_safe=False,
    )
