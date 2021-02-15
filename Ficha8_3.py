def triplica(tuplo):
    tuplo_triplica = ()
    for i in tuplo:
        tuplo_triplica = tuplo_triplica + (i,i,i)
    return tuplo_triplica
tup = (2,0)
print(triplica(tup))