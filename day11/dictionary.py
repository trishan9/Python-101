info = {
    "name": "Trishan",
    "age": 17
}
print(info["name"])
print(info.get("age"))  # c it doesn't throw error irrespective of invalid key
print(info.keys())
print(info.values())
for key in info:
    print(f"{key}: {info[key]}")

for key, value in info.items():
    print(f"{key}: {value}")

dict1 = {1: "trishan", 2: "wagle"}
dict2 = {"1": "trishan", "2": "wagle"}
dict1.update(dict2)
print(dict1)

dict2.clear()
print(dict2)
# del dict1["1"]
# print(dict1)
dict1.pop("2")
dict1.popitem()
print(dict1)
