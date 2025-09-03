class cuadrado_cubo:
    def cuadrado(x):
        numero_cuadrado = x**2
        return numero_cuadrado
    def cubo(x):
        numero_cubo = x**3
        return numero_cubo

def main():
    x=float(input("Ingrese un numero:"))
    print(f"El cuadrado del numero {x} es: {cuadrado_cubo.cuadrado(x)}")
    print(f"El cubo del numero {x} es: {cuadrado_cubo.cubo(x)} ")

main()
        