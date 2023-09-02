################################### DAY 2 PROJECT 4 - Tip Calculator ###################################
total_bill = float(input("Total Bill to Pay: $"))
tip_percentage = float(input("What % tip do you want to give? "))
total_people = int(input("How many people to split the bill? "))

total_amount_to_pay = total_bill + (tip_percentage/100) * total_bill
print(f"Each person should pay: ${round((total_amount_to_pay/total_people), 2)}")