


def simple_decorator(func):
        def wrapper():
            print("Dear customer,")
            func()
            print("Yours Sincerely, Management")
        return wrapper


@simple_decorator
def greet():
        print("We hope you had a good stay at our hotel")


print (greet())
