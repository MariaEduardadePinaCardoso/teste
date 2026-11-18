estoque = 50# definir o estoque inicial
nome = input("quem está retirando: ")# perguntar quem está retirando
quantidade = int(input("quantos pares de luva: "))# perguntar a quantidade de luvas

if quantidade <= 0:# verificar se a quantidade é válida
    print("quantidae inválida.")
elif quantidade > estoque:# verificar se há estoque suficiente
    print(f"estoque insuficiente. disponível{estoque}")
else:# registrar a retirada
    estoque -= quantidade 
    print(f"retira registrada para {nome}. saldo: {estoque}")
if estoque < 10:# avisar se o estoque estiver baixo
    print("atenção: avisar o setor da compras.")

