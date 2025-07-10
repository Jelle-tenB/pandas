import pandas

data = pandas.read_csv(r".\day 25\squirrel_census.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv(r"day 25\squirrel color count.csv")
