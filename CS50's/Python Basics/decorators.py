

def announce_function(f):
    def wrapper_function():
        print("started")
        f()
        print("Ended")
    return wrapper_function

@announce_function
def hello():
    print("hello")

hello()