from functools import wraps
import logging

import config
logger = logging.getLogger('default')


def profile(f):
    """A wrapper for profiling function calls"""
    @wraps
    def wrapper(*args, **kargs):
        logger.debug(f"STARTED:  {f.__name__}")
        res = f(*args, **kargs)
        logger.debug(f"FINISHED: {f.__name__}")
        return res
    return wrapper
