input = int(input())

fahrenheit = 50 + ((input-40)/4)
celcius = 10 + ((input - 40) / 7)

# Deze werken niet door parse problemen.
# print("temperatuur (Fahrenheit): " + fahrenheit)
# print("temperatuur (Celcius): " + celcius)

print(f"temperatuur (Fahrenheit): {fahrenheit}")
print(f"temperatuur (Celsius): {celcius}")