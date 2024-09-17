def analyze_weather_data(temperature_readings):
    if len(temperature_readings) == 0:
        return "No temperature readings available."

    average_temp = sum(temperature_readings) / len(temperature_readings)
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)

    return average_temp, highest_temp, lowest_temp

temperature_readings = list(map(int, input("Enter temperature readings: ").split()))

average, highest, lowest = analyze_weather_data(temperature_readings)

print(f"Average Temperature: {average:.1f}")
print(f"Highest Temperature: {highest}")
print(f"Lowest Temperature: {lowest}")
