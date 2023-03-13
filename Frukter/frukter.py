import random

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här")

frukter =("Apelsin","Banan","Kiwi","Citron","Äpple")

looping = True

while looping:
    i = 1
    print("--------------------")
    print("\n :Fruktautomat: \n")
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1

    fruktnr = input("\nMata in siffra för vald frukt: ")
    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till?\n")


    if (go == "nej"):
        break
print("\n----------------------------------\n")

print("Förresten här får du en frukt till!")
slumpfrukt = random.randint(1, 5)
print_fruit(slumpfrukt)