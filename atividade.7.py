#Aqui inserimos os valores de cada moeda
um_centavo = 0.01
cinco_centavos = 0.05
dez_centavos = 0.10
vinte_cinco_centavos = 0.25 
cinquenta_centavos = 0.50
um_real = 1
#aqui pedimos a quantidade de cada moeda que ele tem
moedas_01 = float(input("Digite quantas moedas de 1 centavo você tem: "))
moedas_5 = float(input("Digite quantas moedas de 5 centavos você tem: "))
moedas_10 = float(input("Digite quantas moedas de 10 centavos você tem: "))
moedas_25 = float(input("Digite quantas moedas de 25 centavos você tem: "))
moedas_50 = float(input("Digite quantas moedas de 50 centavos você tem: "))
moedas_1 = float(input("Digite quantas moedas de 1 real você tem: "))
#aqui está fazendo a multiplicação das moedas
total_moedas = (um_centavo * moedas_01) + (cinco_centavos * moedas_5) + (dez_centavos * moedas_10) + (vinte_cinco_centavos * moedas_25) + (cinquenta_centavos * moedas_50) + (um_real * moedas_1)
#aqui está o resultado de quantas moedas de cada ele tem e a quantdade total
print(f"Você economizou R$ {um_centavo * moedas_01} reais em moedas de 1 centavo")
print(f"Você economizou R$ {cinco_centavos * moedas_5} reais em moedas de 5 centavos")
print(f"Você economizou R$ {dez_centavos * moedas_10} reais em moedas de 10 centavos")
print(f"Você economizou R$ {vinte_cinco_centavos * moedas_25} reais em moedas de 25 centavos")
print(f"Você economizou R$ {cinquenta_centavos * moedas_50} reais em moedas de 50 centavos")
print(f"Você economizou R$ {um_real * moedas_1} reais em moedas de 1 real")
print(f" No total você economizou {total_moedas} Reais em moedas")