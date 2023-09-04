# ################################### High Score ###################################

# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x  

student_scores = input("Input a list of student scores ").split()
highest_score = 0

for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)
print(f"The highest score in the class is: {str(highest_score)}")