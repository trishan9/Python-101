# import csv
import pandas as pd

# with open("weather-data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)


weather_dataframe = pd.read_csv("weather-data.csv")
temperature_series = weather_dataframe["temp"]
# temperatures = temperature_series.to_list()
# print(sum(temperatures) / len(temperatures))
print(temperature_series.mean())
print(temperature_series.max())

# To get particular row
print(weather_dataframe[weather_dataframe.temp == temperature_series.max()])


result = {
    "students" : ["Trishan", "Nischay", "Abiral"],
    "gpa": [3.85, 3.51, 3.91]
}
result_data = pd.DataFrame(result)
result_data.to_csv("result.csv")