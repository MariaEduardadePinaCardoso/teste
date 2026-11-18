def calcular_frete(valor):# função para calcular o frete
    if valor >= 500:# se o pedido for de 500 ou mais
        return 0# frete grátis
    else:
        return 35# frete de 35 reais


quantidade = int(input("quantidade de caixas: "))# ler a quantidade de caixas
preco = float(input("preço de cada caixa: "))# ler o preço de cada caixa

valor_produtos = quantidade * preco# calcular o valor dos produtos

frete = calcular_frete(valor_produtos)# calcular o frete usando a função

total = valor_produtos + frete# somar os produtos com o frete

print(f"valor dos produtos: R$ {valor_produtos:.2f}")# mostrar os resultados
print(f"frete: R$ {frete:.2f}")
print(f"total do pedido: R$ {total:.2f}")