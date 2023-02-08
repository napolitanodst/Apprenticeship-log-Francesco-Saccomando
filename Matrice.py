def matrix(x, y):
    matrix = []

    for i in range(x):
        n = []

        for j in range(y):
            number = 100
            n.insert(i, number)

        matrix.append(n)

    return matrix


x = int(input('inserisci la dimensione x della matrice '))
y = int(input('inserisci la dimensione y della matrice '))

print(matrix(x, y))