#Ejercicio Resuelto 5#
class ejercico5:
    def valor_suma(SUMA, X, Y):
        SUMA = SUMA + X
        X = X + Y**2
        SUMA = SUMA + (X/Y)
        return SUMA
    
#con valores propuestos#
def main():

    SUMA, X, Y = 0, 20, 40
    resultado = ejercico5.valor_suma(SUMA, X, Y)
    print(f"Con los valores SUMA: {SUMA}, X: {X}, y el valor Y: {Y}, El resultado de la suma es {resultado}")

main()