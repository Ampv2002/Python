def soma_quadrados(n):
    soma = 0
    soma_nums = 0
    for i in range(1,n+1):
        soma = i ** 2
        soma_nums = soma_nums + soma
        print(soma_nums)
num = int(input('Digite um número inteiro: '))
soma_quadrados(num)