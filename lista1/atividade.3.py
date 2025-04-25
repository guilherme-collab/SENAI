#pede que insira as horas trabalhadas
qnt_horas_normal = float(input("Digite as horas trabalhadas: ")) 
qnt_horas_extra = float(input("Digite as horas Extras trabalhadas: "))
#define o valor de cada hora
normal = 10
extra = 15
#calculo das horas extras e normais
horas_normal = normal * qnt_horas_normal
horas_extra = extra * qnt_horas_extra
sb = horas_extra + horas_normal
#resultado mostrando salario liquido e o salario bruto
print(f"O salario bruto é de : {sb}")
print(f"O salario liquido é de {sb * 0.90}")