"""
Realpython tutorial
Aug 23 2016
Learn decorator
"""


""" This explain how decorator work """
def my_decorator(some_function):
    def wrapper():
        print("Beginning of wrapper")
        some_function()
        print("End of wrapper")

    return wrapper

def just_some_function():
    print("Whee!")

"""
just_some_function = my_decorator(just_some_function)
just_some_function()
"""

""" Make decorator as module, with out module decorator still working """
if __name__ == "__main__":
    my_decorator()

