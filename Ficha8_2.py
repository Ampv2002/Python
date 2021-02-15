def existe_algarismo(num1,num2):
    var = 0
    while (num1 > 0):
        digito = num1 % 10
        if (digito == num2):
            var = 1
            break
        else:
            num1 = num1 // 10
    if (var == 1):
        return True
    else:
        return False
numero1 = 249435
numero2 = 2
print(existe_algarismo(numero1,numero2))