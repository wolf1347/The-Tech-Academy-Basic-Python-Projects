#
# Python: 3.8
#
# Author: Amber J. Wolf
#
# Purpose: The Tech Academy - Python Course, creating our first program together.
#          Demonstrating how to pass variables from function to function
#          while producing a functional game.
#
#          Remember, function_name(variable) _means we pass in the variable.
#          return Variable _means that we are returning the variable to
#          back to the calling function.


def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_name(f_name, l_name, age, gender)

def get_name(f_name, l_name, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))























if __name__ == "__main__":
    start()
