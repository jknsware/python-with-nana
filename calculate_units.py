calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    else:
        return "You entered a negative value so no conversion for you."

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)