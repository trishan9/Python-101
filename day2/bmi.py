# ################################### BMI Calculator ###################################
weight = int(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))

bmi = weight/(height * height)
print(f"Your BMI is {bmi}")