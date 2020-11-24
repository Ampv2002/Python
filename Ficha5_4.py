def junta_ordenados(t1,t2):
    junta = ()
    i = 0
    j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            junta = junta + (t1[i],)
            i = i + 1
        else:
            junta = junta + (t2[j],)
            j = j + 1
    junta = junta + t1[i:] + t2[j:]
    return junta
um = (2,34,200,210)
dois = (1,23)
print(junta_ordenados(um,dois))