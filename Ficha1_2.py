print("Digite a distancia percorrida em Km:")
distancia = float(input())
print("Digite o tempo que demorou a percorrer essa distância em minutos:")
tempo = float(input())
tempo_horas = tempo / 60
tempo_segundos = tempo * 60
distancia_metros = distancia * 1000
velocidade_media1 = distancia / tempo_horas
velocidade_media2 = distancia_metros / tempo_segundos
print("A velocidade média em Km/h é:",velocidade_media1)
print("A velocidade média em m/s é:", velocidade_media2)