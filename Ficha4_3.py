def filtra_paresTuplos(t1):
    novoTuplo = ()
    for element in t1:
        if (element%2 == 0):
            novoTuplo = novoTuplo + (element,)
    return novoTuplo
t1 = (2,5,6,7,9,1,8,8)
print(filtra_paresTuplos(t1))
