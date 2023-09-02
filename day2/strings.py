############### STRING METHODS
# Multiline Strings
print("""
Handling user authentication is the foundation of application security. The right people should be allowed in, and the wrong people should be kept out. This is done by validating the identity of the person seeking access and then checking whether the person is authorized to enter or not.

In this article, I will give you a step-by-step walkthrough for creating a login page to authenticate the credentials and protect the routes in React application. I will also demonstrate how to limit access to certain web pages, to keep private data safe from guest users.

Add Authentication and Secure the Routes in 9 Easy Steps
Start a New React App.
Install React Router.
Install React Bootstrap UI Library.
Install Axios.
Create a Login Page.
Perform an API Call From Login Page and Store User Token.
Create a Protected Route Utility.
Create a Portal Home Page and Protect the Route.
Register Routes and Protect Them.
""")

# Slicing
language = "JavaScript"
print(language[:4])
print(language[4:])
print(language[-2:]) # -2 is length of language -2 

# Methods
name = "trishAn Wagle -------------"
full_form = "hypEr text markup language"
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.capitalize())
if(full_form.istitle()):
    print(full_form)
else:
    print(full_form.title())
print(name.rstrip("-"))
print(name.replace("-", "!"))
print(name.split(" "), type(name.split(" ")))
print(name.center(50))
print(name.count("-"))
# print(name.startswith("tri", start, end))
print(name.startswith("tri"))
print(name.endswith("-"))
print(name.find("Wag"))
print(name.index("Wag"))
print(name.isalnum())
print(name.isalpha())
print(language.isalnum())
print(name.islower())
