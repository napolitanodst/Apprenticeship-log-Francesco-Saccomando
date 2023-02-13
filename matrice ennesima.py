matrice = []
x = int(input("Inserisci numero righe:"))
y = int(input("Inserisci numero colonne"))
for i in range (x):
     num = []
     for j in range (y) :
          n = int(input("Inserisci un numero"))
          num.insert (i,n)
     matrice.append(num)

print(matrice)