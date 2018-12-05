def adding_report(report = "T"):
    Items = ""
    Total = 0
    print("Input an integer to add to the total or \"Q\" to quit:")
    while True:
        positive_integer = input("Enter an integer or  \"Q\": ")
        if positive_integer.isdigit():
            Total = Total + int(positive_integer)
            if report == "A":
                Items = Items + "\n" +positive_integer
        elif positive_integer.lower().startswith("q"):
            if report == "A":
                print("Items\n" ,Items,"\nTotal\n",Total)
                break
            elif report == "T":
                print(Total)
                break
        else:
            print("input is invalid")



