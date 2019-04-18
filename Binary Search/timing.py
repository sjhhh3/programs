from time import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        endtime = time() - start
        if not endtime:
            print(f'Function "{func.__name__}" with arguments of "{args[0]}" runs too fast, cannot calculate runtime')
        else:
            print(f'Function "{func.__name__}" with arguments of "{args[0]}" runs in {(time()-start)*1000} milliseconds')
    return wrapper

