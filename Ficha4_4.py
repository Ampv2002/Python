def duplicaTuplos(t1):
    novoTuplo = ()
    for i in t1:
        novoTuplo = novoTuplo + (i,i)
        print(novoTuplo)
    return novoTuplo
tuplo = (1,2,3)
duplicaTuplos(tuplo)