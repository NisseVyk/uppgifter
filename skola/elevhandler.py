class Elevhandler:
    def __init__(self):
        self.elevlista = []
        self.filnamn = "elever.pkl"


    def print_menu(self):
        
        print("\n---------Menu---------\n______________________\n|                    |\n|                    |")
        print("| 1. Lista elever    |\n| 2. Lägg till elev  |\n| 3. Ta bort elev    |\n| 4. Avsluta         |\n|                    |\n|____________________|\n")

        val = input ("Mata in ett val: ")
        return val