"""
Simplify logging configuration
"""


import logging
import logging.config
import logging.handlers


DEFAULT_LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s -- %(module)s:%(lineno)d",
        },
    },
    "handlers": {
        "stderr": {
            "level": "WARNING",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "DEBUG",
            "formatter": "detailed",
            "class": "logging.NullHandler",  # no-op by default
        },
    },
    "loggers": {
        "__target": {  # __target will be replaced by logger's name
            "handlers": ["stderr", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


def setup(toplevel_name, config_dict=None, filename=None, file_settings=None):
    """
    Sensible logging configuration

    Set up logging with sensible defaults for whole package referred to by
    toplevel_name.

    Return logger for the toplevel_name. Passing this object around is not
    necessary, because logging.getLogger(toplevel_name) will always refer to
    the same object.

    Arguments:
    toplevel_name
        Name of the module or the package to apply configuration to. The same
        configuration will automatically apply for all child loggers.

    config_dict
        If provided, use these settings instead of defaults. This dictionary
        has to contain settings for "__target" logger.

        For config_dict schema see DEFAULT_LOG_CONFIG in this module and Python
        documentation for logging.config module.

    filename
        If provided, use this file to setup rotating logging. When using custom
        config_dict make sure it contains a handler named "file"

    file_settings
        When filename is provided, use this dictionary to override default setup
        for RotatingFileHandler.
    """
    if config_dict is None:
        config_dict = DEFAULT_LOG_CONFIG

    if filename is not None:
        file_config = config_dict["handlers"]["file"]
        rotating_config = {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": filename,
            "maxBytes": 5*(2**20),  # 5 MiB
            "backupCount": 3,
            "encoding": "utf-8",
        }
        if file_settings:
            rotating_config.update(file_settings)
        file_config.update(rotating_config)

    target = "__target"  # must be hardcoded in config_dict
    if toplevel_name != target:
        loggers = config_dict["loggers"]
        loggers[toplevel_name] = loggers.pop(target, dict())

    logging.config.dictConfig(config_dict)
    return logging.getLogger(toplevel_name)
