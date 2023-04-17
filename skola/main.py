import elevhandler
looping = True
elevhand = elevhandler.Elevhandler()

while looping:
    val = elevhand.print_menu()
    
    if val == "1":
        print("Val 1")

    elif val == "2":
        print("Val 2")
    
    elif val == "3":
        print("Val 3")

    else:
        break

