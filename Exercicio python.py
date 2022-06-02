def diagonalDifference(matriz):
    somaDiagPrincp = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                somaDiagPrincp += matriz[i][j]
    print("a soma da diagonal principal é: " ,somaDiagPrincp)
    print(15* '-=')

    somaDiagSecond = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz)-1:
                somaDiagSecond += matriz[i][j]
    print("A Soma da diagonal secundária: " ,somaDiagSecond)
    print(15* '-=')

    DifDasDiagonais = somaDiagSecond - somaDiagPrincp


    print("A soma das diagonais é: " ,abs(DifDasDiagonais))




matriz = []
elements = []

for i in range(3): # Linhas
    for j in range(3): # Colunas
        elements.append(int(input('Numero:')))
    matriz.append(elements) 
    elements = []


print(matriz)
print(15* '-=')
print(diagonalDifference(matriz))


