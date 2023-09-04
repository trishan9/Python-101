password = "trishan123"
pw_input = ""

while pw_input != password:
    pw_input = input("Enter your password: ")
else:
    print("Logged in Succesfully!")

# break and continue
for i in range (1, 15):
    if i % 2 == 0:
        continue
    if i >= 10:
        break
    print (i)