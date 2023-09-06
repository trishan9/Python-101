languages = ["Java", "JavaScript", "Python", "C++", "C", "GO", "Rust", 1]

tup = (1, 2, 3)
print(tup, type(tup))

# Tuples are immutable, so we don't have such methods to manipulate tuples
# But, if we want to make some change then: first we convert the tuple to a list and again convert it back to tuple using typecasting.

list = list(tup)
list.extend(languages)
tup = tuple(list)
print(tup)

# Like above, we can use all methods of list and change the data type back to tuples if we want to do operations on tuples.

# Slicing, and other lists methods which cannot change the list itself can be used aas tuple method as well, for eg:
c = tup.count(1)
print(c)

i = tup.index("JavaScript")
print(i)

# Print, JavaScript, C++ and Go only with Tuple Slicing
print(tup[4:-1:2])