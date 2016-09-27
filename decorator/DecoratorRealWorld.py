import time
from functools import wraps

def timing_function(some_function):
    """
    Outputs the time function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 -t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in range(10000):
        num_list.append(num)
    print("\nSum of all numbers: " + str(sum(num_list)))


""" decorator using wraps """
def timing_function_2(func):
    @wraps(func)
    def decorated_function():
        t1 = time.time() 
        func()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return decorated_function

@timing_function_2
def my_function_2():
    num_list = []
    for num in range(10000):
        num_list.append(num)
    print("\nSum of all numbers: " + str(sum(num_list)))

""" Practice to write timing wrapper for Fibonaci """
def timing_decorator(func):
    @wraps(func)
    def decorated_func(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        return "Time to execute function: " + str((t2 -t1)) + "\n"
    return decorated_func

@timing_decorator
def my_fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return my_fibonaci(n-1) + my_fibonaci(n-2)


if __name__ == "__main__":
    print(my_fibonaci(42))
