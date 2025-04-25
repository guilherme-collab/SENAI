lata_350ml = float(input("Quantas latas de 350ml  você deseja: ")) #pede que insira quantas latas de 350ml o cliente deseja
garrafa_600ml = float(input("Quantas garrafas de 600ml deseja:")) #pede que insira quantas garrafas de 600ml o cliente deseja
garrafa_2l = float(input("Quantas garrafas de 2l deseja:")) #pede que insira quantas garrafas de 2l o cliente deseja
litros_350ml = 0.350 * lata_350ml
litros_600ml = 0.600 * garrafa_600ml
litros_2l = 2 * garrafa_2l
calculo = litros_2l + (litros_350ml + litros_600ml)
print(f"Você comprou {calculo} litros de refrigerante Meia - Cola")
