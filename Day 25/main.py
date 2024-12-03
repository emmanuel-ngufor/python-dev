import pandas as pd

# data = pd.read_csv("weather_data.csv")

# print(data)


# Get a data column
# print(data["condition"])
# print(data.condition)

# Get Data in row
# print(data[data.day == "Monday"])

# Row with the highest temp in the week
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# new_temp = (monday.temp[0] * 9/5) + 32
# print(new_temp)


# Create a dataframe from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# =============================================

# Read data from csv file and analyse it
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# get counts of Fur colors
gray_count = len ( data [ data["Primary Fur Color"] == "Gray"  ] )
cinnamon_count = len ( data [ data["Primary Fur Color"] == "Cinnamon"  ] )
black_count = len ( data [ data["Primary Fur Color"] == "Black"  ] )

# Create the dictionary version
data_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# convert it to a csv file
new_data = pd.DataFrame(data_dict)
print(new_data)

new_data.to_csv("squirrel_count.csv")

# print(data.info())