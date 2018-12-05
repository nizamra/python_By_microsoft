def rainbow_colors():
    color= input("of a favorite rainbow color first letter: ")
    if color.upper() == "R":
        return("color is Red")
    elif color.upper() == "O":
        return("color is Orange")
    elif color.upper() == "Y":
        return("color is Yellow")
    elif color.upper() == "G":
        return("color is Green")
    elif color.upper() == "B":
        return("color is Blue")
    elif color.upper() == "I":
        return("color is Indigo")
    elif color.upper() == "V":
        return("color is Violet")
    else:
        return ("I'm sorry there is no match")

my_choice = rainbow_colors()
print(my_choice)


def age_20():
    age=input("Please provide your age: ")
    if age.isdigit():
        age=int(age)
        if age < 20 :
            print("You will be 20 in ", 20-age, "years")
        elif age > 20 :
            print("it has been", age-20, "years since you where 20")
        else:
            print("Horray you are 20 years old")
    else:
        print("I'm sorry there seems to be some mistake")


