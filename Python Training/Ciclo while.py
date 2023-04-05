i,n = 0,10
s = 0
while i < n:
    j= int(input("Inserisci un numero:"))
    i+=1
    while 100 <= j <= 1000:
        s+=j
        break
media= s/n
print("La media dei numeri compresi tra 100 e 1000 è:",media)


