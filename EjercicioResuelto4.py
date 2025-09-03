## Ejercicio resuelto 4 ##
class edad_familia:
    @staticmethod
    def calc_edades(edjuan):
        edad_alberto = int(edjuan*(2/3))
        edad_ana = int(edjuan*(4/3))
        edad_mama = edjuan + edad_alberto + edad_ana
        return edad_alberto, edad_ana, edad_mama

def main():
    edad_juan=int(input())
    edad_alberto, edad_ana, edad_mama = edad_familia.calc_edades(edad_juan)
    print(f"Edad de Juan: {edad_juan}")
    print(f"Edad de Alberto: {edad_alberto}")
    print(f"Edad de la Ana: {edad_ana}")
    print(f"Edad de la Madre: {edad_mama}")

main()
