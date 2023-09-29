import pandas

data = pandas.read_csv("squirrel.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_color_count = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}
new_data = pandas.DataFrame(squirrel_color_count)
new_data.to_csv("squirrel_color_count.csv")