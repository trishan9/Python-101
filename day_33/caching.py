from functools import lru_cache
from time import sleep


@lru_cache(maxsize=None)
def sum(a, b):
    sleep(5)
    return a + b


print(sum(2, 3))
print(sum(2, 4))

print(sum(2, 3))
print(sum(2, 4))
