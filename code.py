# Temperature Converter

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2 to choose conversion: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius,  "Celsius is", round(fahrenheit, 2), "Fahrenheit.")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit, "Fahrenheit is", round(celsius, 2), "Celsius.")

else:
    print("Invalid choice. Please enter 1 or 2.")
