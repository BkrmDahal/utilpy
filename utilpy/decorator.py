from threading import Thread
import cProfile, pstats, io
import os
import errno
import signal
from functools import wraps

class _TimeoutError(Exception):
    """Time out error"""
    pass

def profile(fnc):
    
    """
    A decorator that uses cProfile to profile a function
    And print the result
    """
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

def threading_d(func):
  
    """
    A decorator to run function in background on thread
    
	Args:
		func:``function``
			Function with args
	
	Return:
		background_thread: ``Thread``
		
    """
    @wraps(func)
    def wrapper(*args, **kwags):
        background_thread = Thread(target=func, args=(*args , ))
        background_thread.daemon = True
        background_thread.start()
        return background_thread
    return wrapper


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    """
    Decorator to throw timeout error, if function doesnt complete in certain time
    
    Args:
        seconds:``int``
            No of seconds to wait
        error_message:``str``
            Error message
            
    """
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise _TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator