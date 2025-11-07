import time
# we are going to calculate the timing in which the function is execute so thats why we import time
# using *args we can take many arguments
# using **kwargs we can take arguments in the form of key and value
# @timer is decorator when we use function with @ on any function that function have to go through that decorator function

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (f"{func.__name__} took {end - start} seconds.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    print("hello world")

example_function(7)
