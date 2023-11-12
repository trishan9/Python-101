ages = []
# while True:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         break
#     ages.append(age)

# print(ages)

while (age := int(input("Enter your age: "))) >= 18:
    ages.append(age)

print(ages)
