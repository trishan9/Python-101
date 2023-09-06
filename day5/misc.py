# String Formatting
print ("My name is {} and I am {} years old".format("Trishan", 17))
print ("My name is {1} and I am {0} years old".format(17, "Trishan"))
print ("My name is {name} and I am {age} years old".format(age=17, name="Trishan"))

details = "Name={name} Age={age} Batch={batch} College={college}"
print(details.format(name="Trishan Wagle", age=17, batch=35, college="Softwarica"))

# Now from Python3 we use f-Strings instead of traditional String Formatting, which makes our life easier
name = "Trishan"
age = 17
batch = 35
college = "Softwarica"
my_details = f"Name={name} Age={age} Batch={batch} College={college}"
print(my_details)


# Controversial ''' or """
# It has 3 usecases:

# 1st: Using as Multiline Comments, eg:
'''
This is comment and is ignored by Interpreter
'''

# 2nd: Using to format Strings, eg:
string  = f'''
Hello World,

I am {name}

Hello Namaste
'''
print(string)

# 3rd: Doc-Strings (not ignored by Python Interpreter, instead can be accessed by using __doc__ attribute)
# Doc-Strings are very helpful to give short description of function, class or any modules
# It is great for code documentation and also regarded as best practices of Python.
def greet_user ():
    '''It is the function which greets the user when they run the program''' # must be right after function definition, before function body
    print("Namaste, Welcome to Python")
print(greet_user.__doc__)


# PEP-8 (Python Enhanchement Proposal)
# - Style Guide for Python Code: https://peps.python.org/pep-0008/

# It prints The Zen of Python Poem (easter egg) which is very helpful
import this

# Identity Operator
a = 5
b = 7
print (a is b)
a = 10
b = 10
print (a is not b)