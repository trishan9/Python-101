# Recursions are those functions which can call themselves

def fact (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(4))
# 4 * fact(3)
# 4 * 3 * fact(2)
# 4 * 3 * 2 * fact(1)
# 4 * 3 * 2 * 1

# Fibonacci
def fibo (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1;
    else:
        return fibo(n-1) + fibo (n-2)
    
num_of_terms = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(num_of_terms):
    print(fibo(i), end=" ")
print ("\nRecursion! ")