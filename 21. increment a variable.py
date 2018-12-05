#Incrementing
#votes = votes + 1     or   votes += 1
#Decrementing (negative incrementing)
#votes = votes - 1     or   votes -= 1

# [ ] review the SEAT COUNT code then run 

seat_count = 0
while True:
    print("seat count:",seat_count)
    seat_count = seat_count + 1

    if seat_count > 4:
        break


# initialize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4
# loops tallying seats using soft pads vs hard, until seats full or user "exits"
while True:
    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')
    
    if seat_type.lower().startswith("e"):
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1  
    seat_count += 1
    if seat_count >= num_seats:
        print("\nseats are full")
        break
    print(seat_count,"Seats Total: ",hard_seats,"hard and",soft_seats,"soft" )



def Shirt_Count():
    S=0
    M=0
    L=0
    while True:
        size = input("enter the needed sizes (S, M, L), then enter exit to finish: ")
        if size.upper()=="S":
            S +=1
            print()
        elif size.upper()=="M":
            M += 1
            print()
        elif size.upper()=="L":
            L += 1
            print()
        elif size.upper().startswith("E"):
            break
        else:
            print("invalid entry choices are \"S,M,L and exit\"")

    print("\npurchaised Shirt's Count is as follows:\n ", S ,"Small",M,"Medium and ",L,"Large sized shirts")
    print("subtotal costs are:\n ", S*6 ,"for Small shirts",M*7,"for Medium shirts and ",L*8,"for Large sized shirts")
    print("total cost is:\n ", S*6+M*7+L*8,"for all purchaised Shirt's")
    print("PS: prices are all in $")


num_1 = ""
num_temp = ""
num_final = ""
print(num_1,num_temp,num_final)
while True:
    num_1 = input("Enter an integer: ")
    if num_1.isdigit():
        num_final = num_temp + num_1 # this fucked up shit didn't add numbers
        # it concatenated alphabitical characters
        num_temp = num_final
    else:
        print(num_1,num_temp,num_final)
        print(num_final)
        break

x = 0 
while True:
    if x < 10:
        print('run forever')
        x += 1
    else:
        break


time = 3
while True:
    print('time is', time)
    if time == 3:
        time = 4
    else:
        break