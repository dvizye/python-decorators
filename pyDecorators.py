#Decorators

# Add memoization
def memoize(f):
    cache = {}
    
    def wrapper(*args):
        result = cache.get(args) 
        if result == None:
            result = f(*args)
            cache[args] = result
        return result
    return wrapper

# Time execution of function
def timed(f):
    import time as timer
    def wrapper(*args):
        start = timer.clock()
        result = f(*args)
        elapsed = (timer.clock() - start)
        print ('Seconds elapsed for %s: %f ' %(f.__name__, elapsed))
        return result
    return wrapper

# Adds debugging to function
def debug(fn):

    def wrapper(*args):
        result = fn(*args)
        print '{0}{1} : {2}'.format(fn.__name__, args, result)
        return result

    return wrapper

#Examples
@timed
def loop(n):
    print 'executing'
    for i in range(n):
        for j in range(10000):
            pass
@debug        
@memoize
def fibonnaci(n):
    if n == 0 or n == 1:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)
