def soma_quadrados_while(lista):
    i = 0
    soma_quadrados = 0
    while (i < len(lista)):
        soma_quadrados = soma_quadrados + (lista[i]**2)
        i = i + 1
    print("Soma dos quadrados: ",soma_quadrados)
def soma_quadrados_for(lista):
    soma_quadrados = 0
    for i in range(len(lista)):
        soma_quadrados = soma_quadrados + (lista[i]**2)
    print("Soma dos quadrados: ",soma_quadrados)
lista = [1,2,3]
soma_quadrados_while(lista)
soma_quadrados_for(lista)