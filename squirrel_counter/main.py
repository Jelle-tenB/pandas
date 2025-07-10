import pandas

data = pandas.read_csv(r".\day 25\weather_data.csv")

data_dict = data.to_dict()

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

print(data[data.temp == data["temp"].max()])
