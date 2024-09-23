# ========== PSEUDO CODE ==========
# || ACTUAL CODE ||
# - Ask user to input a positive or negative float number for temperature.
inputted_temperature_value_from_the_user = float(input("Input a temperature: "))


# - Formula of the conversion celsius to fahrenheit, vice versa
celsius_to_fahrenheit = inputted_temperature_value_from_the_user*(9/5)+32
fahrenheit_to_celsius = (inputted_temperature_value_from_the_user-32)*(5/9)

# - Ask user user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
print()
print("What conversion type do you want?\nChoose one.\n1 = Celsius to Fahrenheit\n2 = Fahrenheit to Celcius")
ask_conversion_type = input("Write your choice here: ")
    # - Conditional Statement below
if ask_conversion_type == "1":
    print(f"The result of celsius to fahrenheit is {celsius_to_fahrenheit}.")
elif ask_conversion_type == "2":
    print(f"The result of fahrenheit to celsius is {fahrenheit_to_celsius}.")
else:
    print("Invalid input")



