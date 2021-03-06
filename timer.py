import functools

import time

from datetime import datetime

def timer(func):
    
    """Timer function to display the time it takes for another function to complete."""
    
    @functools.wraps(func)
    
    def wrapper_timer(*args, **kwargs):
        
        start_time = time.perf_counter() # 1
        
        value = func(*args, **kwargs)
        
        end_time = time.perf_counter() # 2
        
        run_time = end_time - start_time
        
        print(f"On {datetime.today().strftime('%Y %d %T')} the function {func.__name__!r} finished in {secondsToText(run_time)}")
        
        return value
    
    return wrapper_timer

def secondsToText(secs):
    
    """Display time to readable format of Days, Hours, Minutes, and Seconds. Input seconds to receive output."""

    days = secs//86400

    hours = (secs - days*86400)//3600

    minutes = (secs - days*86400 - hours*3600)//60

    seconds = (secs - days*86400 - hours*3600 - minutes*60)

    result = ("{0} day{1}{2}{3}{4}".format(days, "s" if days!=1 else "", ", " if seconds and minutes or minutes and hours or hours and seconds else "", " and " if hours and not minutes and not seconds or minutes and not hours and not seconds or seconds and not hours and not minutes else "", " " if not hours and not minutes and not seconds else "") if days else "") + ("{0} hour{1}{2}{3}{4}".format(hours, "s" if hours!=1 else "", ", " if seconds and minutes else "", " and " if seconds and not minutes or minutes and not seconds else "", " " if not minutes and not seconds else "") if hours else "") + ("{0} minute{1}{2}".format(minutes, "s" if minutes!=1 else "", " and " if seconds else " ") if minutes else "") + ("{0} second{1} ".format(f'{seconds:.2f}', "s" if seconds!=1 else " ") if seconds else "")
    
    return result
