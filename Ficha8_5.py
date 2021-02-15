def soma_quadrados_valores(dic):
    soma_quadrados = 0
    for i in dic:
        soma_quadrados = soma_quadrados + (dic[i]**2)
    return soma_quadrados
dicionario = {'a':2, 'b':5, 'c':3}
print(soma_quadrados_valores(dicionario))