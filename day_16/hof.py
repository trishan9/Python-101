from functools import reduce

l = [1, 2, 3, 4, 5, 6]

# def square(x):
#     return x * x

# l2 = list(map(square, l))
# print(l2)

l2 = list(map(lambda x: x * x, l))
print(l2)

l3 = list(filter(lambda x: x > 3, l))
print(l3)

l4 = reduce(lambda a, b: a + b, l)
print(l4)