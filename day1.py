# Printing
print("Hello Python!")
print("Hello\nPython!")
print("Hello" + " " + "Python!")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# Debugging
# Expected Result:
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

# Solution:
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + '"+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Input Function
print("Hello " + input("What is name\n") + ", Good Morning!")
print(len(input("Enter name\n")))


# Variables
user_name = input("What is name? ")
print(type(user_name))
name_length = len(user_name)
print("Hello " + user_name)
print(name_length)

# Wap to swap two variables in python
a = input("a: ")
b = input("b: ")
temp = a
a = b
b = temp
print("a: " + int(a))
print("b: " + int(b))


################################### DAY 1 PROJECT - EMAIL GENERATOR ###################################
#1. Create a greeting for your program.
#2. Ask the user for their name, company they're applying in, company's hr's name, position they want to apply, job field, where the job was advertised,
# years of experience, skills, what makes them stand out, phone number, email, linkedin profile.
#3. Combine all the details and generate JOB APPLICATION email for them according to their details.

print("\nHello there, Hope you're doing well. Welcome to our JOB APPLICATION generator!\n")

# INPUT FROM THE USER
applicant_name = input("What's your name? \n")
company_name = input("What's the name of the company you're applying in? \n")
hr_name = input("What's the name of " + company_name + "'s HR \n")
position = input("What's the job position you want to apply for? \n")
field = input("In which field/industry are you expert in? \n")
advertised_at = input("From where did you know about the vacant job? \n")
experience = input("Your years of experience? \n")
skills = input("Enter your skills (seperated in comma) \n")
quality = input("What makes you stand out? (separated in comma) \n")
phone = input("Enter your contact number \n")
email = input("Enter your email address \n")
linkedin = input("Enter the link of your LinkedIn Profile \n")

# EMAIL GENERATION
job_application = "Subject: Enthusiastic Applicant Interested in " + position + " Opportunity at " + company_name + "\n\nDear " + hr_name + ",\n" + "\nI hope this email finds you well. My name is " + applicant_name + ", and I am writing to express my strong interest in the " + position + " position at " + company_name + ", as advertised on " + advertised_at + ". With " + experience + " years of experience in " + field + " field" + ", I am excited about the prospect of contributing my skills and expertise to your team.\n" + "\nThroughout my professional journey, I have honed my skills in " + skills + ". My experience has provided me with a deep understanding in " + field + " field.\n" + "What sets me apart is my extra qualities and soft skills like: " + quality + ". I believe this quality aligns well with your company's culture and would contribute to the goals of the company.\n" + "\nI am drawn to " + company_name + " because of its reputation, innovative work in " + field + "field" + ". I am excited about the opportunity to join your team and be a part of the vision of your company.\n" + "\nEnclosed is my resume, which provides additional details about my experience and accomplishments. I am eager to discuss how my skills and background align with the needs of your company and how I can contribute to your continued success.\n" + "\nThank you for considering my application. I look forward to the possibility of discussing how I can make a meaningful contribution to your company in more detail. Please feel free to contact me at " + phone + " or " + email + " to schedule a conversation at your convenience. We can discuss and negotiate on salary, benefits and other. Hoping for your positive response.\n\n" + "Warm regards,\n" + applicant_name + "\n" + "LinkedIn: " + linkedin

print("Here is your job application ready for you, " + applicant_name)
print("We wish you the best for you career\n")
print("GENERATED JOB APPLICATION:")
print(job_application)