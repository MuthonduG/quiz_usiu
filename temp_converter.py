def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula: F = C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Prompt the user for a temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the temperature in Fahrenheit
print(f"The temperature {celsius}°C is equivalent to {fahrenheit}°F")
