#!/usr/bin/python3

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapperTimer(*args, **kwargs):
        startTime = time.perf_counter()
        value = func(*args, **kwargs)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        print(f"Finished {func.__name__!r} in {runTime:.10f} secs")
        return value
    return wrapperTimer