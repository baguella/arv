import personbil
import lastbil

looping = True

#Initierar 2 st personbils object av classen Personbil
opel_brun = personbil.Personbil("Opel", "Brun", 200)
volvo_svart = personbil.Personbil("Volvo", "Svart", 250)

#Initierar 2 st lastbils object av classen Lastbil
scania_rosa = lastbil.Lastbil("Scania", "Rosa", 40000)
volvobm_orange = lastbil.Lastbil("Volvo BM", "Orange", 50000)

#skapar listor med personbilar och lastbilar
personbils_lista = [opel_brun, volvo_svart]
lastbils_lista = [scania_rosa, volvobm_orange]

#main program
while looping:
    print("----------------------------------------")
    print("\n-:Klasser och arv av fordon:-\n")

    go = input("\n Vill du lista fordon igen? j/n ")
    print("\n")
    
    if (go == "n"):
        break