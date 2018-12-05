#Formatting strings using escape sequences
#escape sequences all start with a backslash (\)
#escape sequences can be used to display characters in python reserved for formatting
#\\   Backslash (\)
#\'   Single quote (')
#\"   Double quote (")
#\t   Tab
#\n   return or newline
#We use escape sequences in strings - usually with print() statements

#Examples
print('Hello World!\nI am formatting print ')
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")
print("for a newline use \\n")
print ("\\\WARNING!///")
print("\"What\'s that?\" isn\'t a specific question.")
print("\tOne\tTwo\tThree")
print("Hello" + "\n" + "World!")
print("\\\\\\\\")

def pre_word():
    single = input("enter a word that starts with \"pre\": ")
    if single.lower().startswith("pre"):
        if single.isalpha():
            print ("is a valid \"pre\" word")
            return True
        else:
            print ("not an alphabitical word")
            return False
            
    else:
        print ("not a \"pre\" word")
        return False