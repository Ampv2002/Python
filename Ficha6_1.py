def remove_multiplos(l1,n):
    NovaLista = []
    for i in range(0,len(l1),1):
        if (l1[i] % num != 0):
            NovaLista.append(l1[i])
    return NovaLista
lista = [2,3,5,9,12,33,34,45]
num = 3
print(remove_multiplos(lista,num))