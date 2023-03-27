import bil

looping = True

Ford_red = bil.bil("Ford", "röd", 5)
Volvo_rosa = bil.bil("Volvo 240", "rosa", 1)
Ferrari_red = bil.bil("Ferrari", "röd", 20)

billista = [ Ford_red, Volvo_rosa, Ferrari_red]

while looping:
    print("-------------------------")
    print("BilAutomat")

    i=0

    for bil in billista:

        print(str(i+1) + " : " + bil.fabrikat +","+ " Färg: " +bil.color +","+ " Lager: " + str(bil.lager))
        i=i+1

    bil_nr = input("\n Mata in siffra för vald bil: ")
    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getLager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print("\n En " + billista[bil_nr_int-1].color + " " + billista[bil_nr_int-1].fabrikat + " kommer här")
        
        nyttlagersaldo_int = lager_int - 1
        nyttlagersaldo_str = str(nyttlagersaldo_int)

        billista[bil_nr_int-1].setLager(nyttlagersaldo_int)

    else:
        print("Tyvärr slut på vald bil")


    svar = input("\n Vill du avsluta programmet? j/n : ")
    if (svar == 'j'):
        break
