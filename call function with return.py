# Message double returns the string Argument doubled
def msg_double(phrase):
      double = phrase + " " + phrase.capitalize()
      return double

# save return value in variable
msg_2x = msg_double("let's go")
print(msg_2x)

# prints the returned object
print(msg_double("Save Now!"))

# echo the type of the returned object
type(msg_double("Save Now!"))

# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(full_name):
    full_name=input("give me your name: ")
    return "Dr "+full_name.capitalize()

