import math
cat_1 = float(input("Introduza o valor do primeiro cateto: "))
cat_2 = float (input("Introduza o valor do segundo cateto: "))
hipotunusa_quadrado = (cat_1*cat_1)+(cat_2*cat_2)
hipotunusa = math.sqrt(hipotunusa_quadrado)
print("O valor da hipotunusa é:", hipotunusa)