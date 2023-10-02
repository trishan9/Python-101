def greet(func):
    def wrapper_accepting_arguments(*args, **kwargs):
        func(*args, **kwargs)
        print("Hello World")
    return wrapper_accepting_arguments


@greet  # equivalent to greet(add())
def add(*args):
    print(sum(args))


add(20, 40, 20, 20)
# greet(add(20, 50))
