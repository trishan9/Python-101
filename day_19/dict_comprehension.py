import random
import pandas

students = ["Trishan", "Nischay", "Abiral"]
result = {student : random.randint(1, 100) for student in students}
print(result)

passed_students = {student : mark for student, mark in result.items() if mark > 40}
print(passed_students)

# Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split(" ")
result = {word:len(word) for word in list_of_words}
print(result)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(celsius * 9/5) + 32 for day, celsius in weather_c.items()}
print(weather_f)


school_result = {
    "students": ["Trishan", "Nischay", "Abiral"],
    "score": [91, 90, 80]
}
dataframe = pandas.DataFrame(school_result)
# for key, value in dataframe.items():
#     print(value)
for index, row in dataframe.iterrows():
    print(row.score)