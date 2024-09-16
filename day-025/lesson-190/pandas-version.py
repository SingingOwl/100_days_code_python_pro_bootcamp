import pandas

def c_to_f(celsius):
    return (celsius * 9/5) + 32

data = pandas.read_csv("weather_data.csv")
print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)
print(f"The average temperature is {average_temp}")

max_temp = data["temp"].max()
print(f"The highest temperature was {max_temp}\n")

print("Monday's temperature was " + str(c_to_f(data[data.day == "Monday"].temp.iloc[0])) + "F\n")

print(data[data.day == "Monday"].temp)

print(data[data.temp == data["temp"].max()])

mon_temp = data[data.day == "Monday"].temp