# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy): ") 

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for", weather)


# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")



# [ ] code and test SHIRT SALE

size = input("Enter a size for the employee to help you (S,M,L): ")

if size.upper() == "S":
    print("the price of this item is $6")
elif size.upper() == "M":
    print("the price of this item is $7")
elif size.upper() == "L":
    print("the price of this item is $8")
elif size.upper() == "XL":
    print("the price of this item is $9")
else:
    print(size, "size is not available/valid")