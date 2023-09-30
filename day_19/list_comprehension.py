num = [1, 2, 3, 4]
squared_num = [ i ** i for i in num if i % 2 == 0]
print(squared_num)

names = ["Trishan", "Nischay", "Abiral"]
upper_case_names = [name.upper() for name in names]
print(upper_case_names)

# Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# Exercise 3
file1 = open("file1.txt")
file2 = open("file2.txt")

file1_nums = [int(num[:-1]) for num in file1.readlines()]
file2_nums = [int(num[:-1]) for num in file2.readlines()]
file1.close()
file2.close()

result = [num for num in file1_nums if num in file2_nums]
print(result)