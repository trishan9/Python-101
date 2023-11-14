from sys import getsizeof

even = [i for i in range(100) if i % 2 == 0]
print(even)
print(getsizeof(even))

even_gen = (i for i in range(100) if i % 2 == 0)
print(list(even_gen))
print(getsizeof(even_gen))


def my_func():
    for i in range(10000):
        yield i


gen = my_func()
print(getsizeof(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for i in gen:
    print(i)
