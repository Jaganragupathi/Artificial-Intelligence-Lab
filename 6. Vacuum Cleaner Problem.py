room = input("Enter room status (A B): ").split()
position = input("Enter vacuum position: ")

while room[0] == "Dirty" or room[1] == "Dirty":
    if position == "A":
        if room[0] == "Dirty":
            print("Clean A")
            room[0] = "Clean"
        else:
            print("Move Right")
            position = "B"
    else:
        if room[1] == "Dirty":
            print("Clean B")
            room[1] = "Clean"
        else:
            print("Move Left")
            position = "A"

print("Both rooms are clean")
