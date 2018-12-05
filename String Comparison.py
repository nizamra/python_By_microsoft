#Strings can be equal == or unequal !=
#Strings can be greater than > or less than <
#alphabetically "A" is less than "B"
#lower case "a" is greater than upper case "A"

# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")
# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")
#Task 2
#Conditionals: comparison operators with if
# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"


def tf_quiz(arg1, arg2):
    
#answer key string like "T"
#Program: True False Quiz Function
#Call the tf_quiz function with 2 arguments

#T/F question string
#answer key string like "T"
#Return a string: "correct" or incorrect"
# Define and use tf_quiz() function
#tf_quiz() has 2 parameters which are both string arguments
#question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
#correct_ans: a string indicating the correct answer, either "T" or "F"
#tf_quiz() returns a string: "correct" or "incorrect"
#Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()
# [ ] Create the program, run tests
    print("words_to_yell")