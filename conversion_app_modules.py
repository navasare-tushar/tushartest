"""

#import conversion_main as cm   -- this can be done or we can do it below way as passing parameters to
#fuction while calling from main

"""
def days_to_units(num_of_days, conversion_unit):
    # print(type(condition_check))  # type is a function which returns data type details
    if conversion_unit == "hours":
        return f"{num_of_days} days are having {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are having {num_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are having {num_of_days * 24 *60 *60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_int = int(days_and_unit_dict["days"])  # after split, each element in list is still a char, converted int
        if user_input_int > 0:
            calculated_value = days_to_units(user_input_int,days_and_unit_dict["unit"])
            print(calculated_value)
        elif user_input_int == 0:
            print("You have entered Zero,Please enter 'exit' to terminate.Thank you!")
        else:
            print("you have entered a negative number,Please enter 'exit' to terminate.")

    except ValueError:
        print("Negative input,Please enter 'exit' to terminate.")


user_input_msg = "\nEnter value for number of days and conversion unit (20:hours)\nHi, Or enter 'exit' to terminate\n"
