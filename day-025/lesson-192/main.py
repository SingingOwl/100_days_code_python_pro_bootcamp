import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count_summary = data.groupby('Primary Fur Color').size().reset_index(name='Count')

print(count_summary)