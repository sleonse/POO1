class salario:
    def calcular_salario_bruto(horas_trabajadas, valor_hora):
        salario_bruto = horas_trabajadas * valor_hora
        return salario_bruto
    def calcular_retencion(salario_bruto, porcentaje_retencion):
        retencion = salario_bruto * (porcentaje_retencion/100)
        return retencion
    def calcular_salario_neto(salario_bruto, retencion):
        salario_neto = salario_bruto - retencion
        return salario_bruto

def main():
    #Con los valores dados#
    horas_trabajadas, valor_hora, porcentaje_retencion = 48, 5000, 12.5
    salario_bruto = salario.calcular_salario_bruto(horas_trabajadas, valor_hora)
    retencion = salario.calcular_salario_bruto(salario_bruto, porcentaje_retencion)        
    salario_neto = salario.calcular_salario_bruto(salario_bruto, retencion)
    print(f"Dado que trabajaste {horas_trabajadas} horas, el valor a cobrar por hora es de {valor_hora}$, y el porcentaje de retencionb es de {porcentaje_retencion}%")
    print(f"Tu salario bruto es de: {salario_bruto}$, tu valor retenido es de: {int(retencion)}$, y tu salario neto es de: {int(salario_neto)}$")
main()