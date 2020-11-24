def triangular(n):
    i = 1
    contaT = 0
    soma = 0
    while i <= n:
        if (soma == n):
            contaT = 1
        soma = soma + i
        i = i + 1
    if (contaT > 0):
        return True
    else:
        return False
print(triangular(6))