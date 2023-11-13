from sys import getsizeof


def my_func():
    for i in range(100000):
        yield i


generator = my_func()
# generator = list(generator)
print(getsizeof(generator))
