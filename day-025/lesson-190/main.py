import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    # Skip the header
    next(data)

    # Create a list to store temperatures
    temperatures = []

    # Iterate through the rows and append the temperature values
    for row in data:
        temperatures.append(int(row[1]))  # Convert temperature from string to integer

print(temperatures)