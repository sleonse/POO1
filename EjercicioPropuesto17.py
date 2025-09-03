import math

pi = math.pi

class circunferencia:
    def area(radio):
        area = (radio**2) * pi
        return area
    def longitud(radio):
        longitud = 2 * radio * pi
        return longitud

def main():
    radio = float(input("ingrese el radio de la circuferencia: "))
    area = circunferencia.area(radio)
    longitud = circunferencia.longitud(radio)
    print(f"Dado que el radio del circulo es de: {radio}, su area es de: {area} y su longitud de arco es de: {longitud}")

main()