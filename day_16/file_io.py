f = open("info.txt", "w")
f.write("1,2,3\n4,5,6\n7,8,9")
f.close()

with open("info.txt", "r") as f:
    print(f.read())

with open("info.txt", "r") as f:
    i = 0
    while True:
        i += 1
        line = f.readline()
        if not line:
            break
        m1 = int(line.split(",")[0])
        m2 = int(line.split(",")[1])
        m3 = int(line.split(",")[2])
        print(f"Marks of student {i} in Maths is: {m1*2}")
        print(f"Marks of student {i} in English is: {m2*2}")
        print(f"Marks of student {i} in SST is: {m3*2}")

f2 = open("new.txt", "r")
f2.seek(5)
print(f2.read(3))
f2.close()

# f3 = open("new.txt", "a")
# f3.write("Trishan")
# f3.truncate(5)
# f3.close()