__author__ = "Sizikov A.S."

import time
import functools
from .write_to_file import write_to_md

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() 
        value = func(*args, **kwargs)    
        end_time = time.perf_counter()   
        run_time = end_time - start_time 
        write_to_md(func.__name__, run_time)
        return value
    return wrapper_timer