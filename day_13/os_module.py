import os

dir = os.listdir(".")
print(dir)
print(os.getcwd())

if not os.path.exists("Trishan"):
    os.mkdir("Trishan")

# for i in range(0, 100):
#     os.mkdir(f"Trishan/Day{i+1}")

# for i in range(0, 100):
#     os.rename(f"Trishan/Day{i+1}", f"Trishan/Tutorials {i+1}")

# for i in range(0, 100):
#     os.rmdir(f"Trishan/Tutorials {i+1}")

os.rmdir("Trishan")