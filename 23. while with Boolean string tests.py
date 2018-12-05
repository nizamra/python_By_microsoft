# review and run example that loops until a valid first name format is entered
student_fname = ""
while student_fname.isalpha() == False:
    student_fname = input("enter student\'s first name (Letters only, No spaces): ")
print("\n" + student_fname.title(),"has been entered as first name")


count = 1
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1

def ignore_case(name):
    answer = ""
    while answer.isalpha() == False:
        answer = input("enter last name: ")
    return answer.lower() == name.lower()


tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")

print("The new line character is \"\\n\"")