# # # Armstrong
# sum_of_num = 0
# for n in (num := input("Enter the number to check Armstrong: ")):
#     sum_of_num += int(n) ** len(num)
# if str(sum_of_num) == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong!")

# # # Palindrome
# # if (num := list(input("Enter the number to check palindrome: "))) == list(reversed(num)):
# #     print("Palindrome!")
# # else:
# #     print("Not Palindrome!")

# if (num := input("Enter the number to check palindrome: ")) == num[::-1]:
#     print("Palindrome!")
# else:
#     print("Not Palindrome!")

# Factorial
# num = 4
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# def fact(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact(n - 1)


# print(fact(4))


# Fibonacci
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)


# for i in range(n := int(input("Enter the number for fibonacci series: "))):
#     print(fibo(i))


# Prime Number
n = int(input("Enter the number to check prime number: "))
is_prime = True
is_divisble_by = 0
if n == 0 or n == 1:
    print("Not a Prime Number!")
elif n == 2:
    print("Prime number!")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            is_divisble_by = i
            break
if is_prime:
    print("Prime number!")
else:
    print(f"Not a Prime Number!, because {n} is divisible by {is_divisble_by}")
