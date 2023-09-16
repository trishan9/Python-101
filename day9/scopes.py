# Local Scopes
def test():
    name = "Trishan"
    print(name)
test()
# print(name) Error because name variable is local scoped inside test function

# There is no Block Scope in Python
if 7 > 5:
    caste = "Wagle"
print(caste) # Can be accessed because variables are local scoped only inside functions not on if blocks, or loop blocks or any other blocks

# Global Scopes
full_name = "Trishan Wagle" # can be accessed anywhere
# but can't be modified directly inside functions/any other blocks which creates local scoped variables. Eg:
def test2():
    # full_name = "Wagle Trishan" # it doesn;t changes our global variable instead it makes new local variable
    # So, to change global variable:
    global full_name
    full_name = "Wagle Trishan" # it now changes our global scoped variable
test2()
print(full_name)