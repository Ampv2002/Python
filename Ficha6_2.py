def junta_ordenadas(l1,l2):
    i = 0
    j = 0
    ListaOrdenada = []
    ListaRestantes = []
    while (i < len(l1)) and (j < len(l2)):
        if l1[i] < l2[j]:
            ListaOrdenada.append(l1[i])
            i += 1
        else:
            ListaOrdenada.append(l2[j])
            j += 1
    ListaRestantes.append(l1[i:ListaOrdenada[i]])
    ListaRestantes.append(l2[j:ListaOrdenada[j]])
    ListaOrdenada.append(ListaRestantes)
    return ListaOrdenada
lista1 = [2,5,90]
lista2 = [3,5,6,12]
print(junta_ordenadas(lista1,lista2))