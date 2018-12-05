greet_count = 5
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
print("\nIGNITION!")


def Animal_Names():
    num_animals = 0
    animal_name = ""
    all_animals = ""
    while num_animals <4:
        animal_name = input("animal name  of 4 animals: ")
        if animal_name.lower().startswith("e"):
            break
        else:
            num_animals +=1
        all_animals = all_animals + " " + animal_name
    
    if all_animals == "":
        print("no animals")
    else:
        print(all_animals)