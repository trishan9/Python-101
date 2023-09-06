languages = ["Java", "JavaScript", "Python", "C++", "C", "GO", "Rust"]

# Membership Operators
if "JavaScript" in languages:
    print ("Yes")
else:
    print("No")

if "React" not in languages:
    print ("True")

# Slicing
print(languages[2::2]) # third argument is stride

# List Comprehension
list = [language for language in languages if len(language) > 5]

# List Methods
languages.append("ReactJS")
languages.insert(0, "NextJS")
languages.extend(["NodeJS", "ExpressJS"])
languages.extend(("MongoDB", "SQL"))
languages.sort()
languages.sort(reverse=True)
languages.reverse()
i = languages.index("JavaScript") #throws error if item not found
c = languages.count("JavaScript")

# Deep Copy = Completely independent copy of original structure, changes made to the copied structure will not affect the original structure because they are entirely separate.
# Shallow Copy = a shallow copy will only copy references to those nested objects, not the nested objects themselves. 
# Therefore, changes made to the nested objects in the copied structure will also affect the original structure, as they share the same nested objects.

# Shallow copy in python:
new_lang = languages
new_lang[0] = "Nepali" # it changes the languages list too

# Deep copy in python:
new_list = languages.copy()
new_list[0] = "English" # it doesn't change the languages list

print(languages)