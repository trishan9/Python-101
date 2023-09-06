empty_set = set()
print(type(empty_set))

set = {2, 4, 1, 2, 3}
print(set)

a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

set.add("Trishan")
set.add("Wagle")
print(set)
set.remove("Wagle")
set.discard("Wagless")
set.pop()
print(set)