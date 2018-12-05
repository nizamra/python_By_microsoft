#
def fishstore(fish , price):
    output = ("Fish Type: ", fish.title() , "costs: $" , price)
    return output

fishstore("guppy", 1)


def make_schedule(period1, period2,period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history","science fiction")
print("SCHEDULE:", student_schedule)


#Fix The Error
# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")