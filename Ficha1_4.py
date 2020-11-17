tempo = float(input('Escreva o número de segundos: '))
dias = tempo // (24 * 3600)
tempo = tempo % (24 * 3600)
horas = tempo // 3600
tempo %= 3600
minutos = tempo // 60
tempo %= 60
segundos = tempo
print("Dias:", dias)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)