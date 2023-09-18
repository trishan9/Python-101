def sum_func(a, b):
    return a + b


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = sum_func(num1, num2)
    print(result)
except Exception as error:
    print(error)
finally:
    print("I am always executed")

print("Important Code Running....")
print("End of the Program")
