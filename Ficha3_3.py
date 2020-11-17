from Ficha3_2 import area_circulo
def area_coroa (r1,r2):
    if (r1>r2):
        raise ValueError
    else:
        area_coroa = area_circulo(area_ext) - area_circulo(area_int)
        return area_coroa
area_ext = eval (input ('Insira raio exterior: '))
area_int = eval (input ('Insira raio interior: '))
print("A area da coroa é = ", area_coroa(area_int, area_ext))