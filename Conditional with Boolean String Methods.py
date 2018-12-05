# review code and run cell
favorite_book = input("Enter the title of a favorite book: ")
if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
else:
    print(favorite_book, "- consider capitalization throughout for book titles.")


# review code and run cell
a_number = input("enter a positive integer number: ")
if a_number.isdigit():
    print(a_number, "is a positive integer")
else:
    print(a_number, "is not a positive integer")  
# another if
if a_number.isalpha():
    print(a_number, "is more like a word")
else:
    pass


# review code and run cell
vehicle_type = input('"enter a type of vehicle that starts with "P": ')
if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


#Task 2: multi-part
#Evaluating Boolean Conditionals
#create evaluations for .islower()
#print output describing if each of the 2 strings is all lower or not
test_string_1 = "welcome"
test_string_2 = "I have $3"
if test_string_1.islower():
    print("Yes it is.")
else:
    print("it's not lower for some reason.")


#Task 2 continued...
#create a functions using startswith('w')
#w_start_test() tests if starts with "w"
#function should have a parameter for test_string and print the test result
#test_string_1 = "welcome"
#test_string_2 = "I have $3"
#test_string_3 = "With a function it's efficient to repeat code"
def w_start_test(phrase):
    if phrase.lower().startswith('w'):
        print('yeah it starts with a "w"')
    else:
        print("Nope it doesn't start with 'w'")

