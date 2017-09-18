"""
General purpose context managers
"""


import sys
import traceback
from contextlib import contextmanager


@contextmanager
def suppress_and_log(*exceptions, logger=None):
    """
    Context manager to suppress specified exceptions verbosely.

    If no exceptions are specified with arguments, use Exception class.

    Suppressed exceptions are logged to stderr by default.
    If logger is specified, exceptions are logged there using logging.ERROR
    priority.

    After the exception is suppressed, execution proceeds with the next
    statement following the with statement.

    See also: contextlib.suppress - same functionality without logging.
    """
    if not exceptions:
        exceptions = Exception
    try:
        yield
    except exceptions as e:
        message = "{} suppressed, see traceback below:".format(type(e).__name__)
        if logger:
            logger.exception(message)
        else:
            print(message, file=sys.stderr)
            traceback.print_exc()
