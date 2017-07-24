"""
Some scripting tools specific to Red Hat's Openshift automation
"""

__all__ = [
    "control",
    "control_isrunning",
]

from .cartridge import control, control_isrunning
