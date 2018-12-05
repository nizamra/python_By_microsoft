#This program requires the use of while loop to get non-empty input, if, else, if, else (nested),
#  .isdigit() check for integer only input, .isalpha() check for alphabetic only input.
# The program should only use code syntax covered in modules 1 - 4.
# The program must result in printed message analysis of the input.

def str_analysis():
    msg = ""
    while msg =="":
        msg = input("enter word or integer: ")
        if msg.isdigit():
            if int(msg)<99:
                print(msg,"is a smaller number than expected")
                break
            elif int(msg)>99:
                print(msg,"is a pretty big number")
                break
            else:
                pass
        elif msg.isalpha():
            print(msg,"is all alphabetical characters!")
            break
        elif msg != "":
            print(msg,"is multiple character types!")
            break
        else:
            pass
            

    
