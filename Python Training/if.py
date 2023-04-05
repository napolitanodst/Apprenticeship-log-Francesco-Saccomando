x = int(input("Inserisci il numeratore della frazione:"))
y = int(input("Inserisci il denominatore della frazione:"))

if x < y :
    print("La frazione è Propria")
elif x > y or x % y !=0:
    print("La frazione è Impropria")
else:
    print ("La frazione è Apparente")


