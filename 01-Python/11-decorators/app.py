def run_three_times(func):
    def wrapper():
        func()
        func()
        func()

    return wrapper

@run_three_times
def say_hi():
    print("Hi !")

say_hi()
