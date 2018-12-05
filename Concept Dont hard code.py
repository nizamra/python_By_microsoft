#
def bird_available():
    x = input("enter a bird name to check for availability: ")
    bird_types = ('crow robin parrot eagle sandpiper hawk pigeon')
    print(x, "availability is", x.lower() in bird_types.lower())

bird_available()

