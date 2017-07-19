# toolpot - An assorted collection of Python tools
You wouldn't expect a professional to store his tools in a clay pot, would you?

![toolpot logo](docs/logo/toolpot.png)


# Package contents
### toolpot.scripting
Tools for day to day OS automation.

Unix shell is an incredibly powerful tool
and writing shell scripts can be very fun, but Python offers ease of use
and reuse far beyond what can be found in shell. Plus Python smoothes a lot of
edge cases (read: string escaping) that can be time consuming to do properly
in bash

### toolpot.python
Use these tools to simplify some repeating tasks when developing in Python

### toolpot.openshift
Some scripting tools specific to Red Hat's Openshift automation

### toolpot.sap
Helper utilites for SAP ERP users. No administrative access to SAP server is
required or assumed


# Installation and usage
This project is (and probably will always be) a work in progress. The only
recommended to use version is the one currently in git repository

Use pip to install the package:
`pip install git+git://github.com/sio/toolpot.git`

After installation use `import toolpot` from your Python scripts


# Contributing
All contributions are welcome!
Please check [CONTRIBUTING.md](CONTRIBUTING.md) for details


# License and copyright
Copyright © 2017 Vitaly Potyarkin
```
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
