num1 = int(input("Enter number between 1 and 5: "))
if num1 < 1 or num1 > 5:
    raise ValueError("Number should be between 1 and 5 only")
print(num1)
