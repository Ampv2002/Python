def juntos(lista):
    aux = lista[0]
    soma = 0
    contaPosicao = 0
    for i in lista:
        if (contaPosicao == 0):
            contaPosicao = 1
        elif(aux == i):
            soma = soma + 1
        aux = i
    return soma
tuplo = [1,2,2,3,4,4]
print(juntos(tuplo))