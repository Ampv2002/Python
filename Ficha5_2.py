def num_divisores(n):
    d = 0
    i = 1
    while i <=n:
        if(n == 0):
            return 0
        if (n % i == 0):
            d = d + 1
        i = i +1
    return d
t1 = int(input('Digite um número inteiro: '))
print(num_divisores(t1))