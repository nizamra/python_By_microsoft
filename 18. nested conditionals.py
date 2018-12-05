sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich") 

else:
    print("Here is your Veggie Special")