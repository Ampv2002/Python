ano = int(input('Escreva um ano para eu dizer se é bissexto: '))
if (ano % 4) == 0 and (ano % 100) != 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
