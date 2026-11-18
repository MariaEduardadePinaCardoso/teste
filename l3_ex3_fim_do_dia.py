estoque = 120 # estoque inicial
total = 0
maior = 0

quantidade_retirada = int(input("quantas retiradas houve hoje?"))# perguntar quantas retiradas houve

for i in range(1, quantidade_retirada + 1):# repetir para cada retirada
    retirada = int(input(f"retirada {i}: "))
    
total = total + retirada# somar as retiradas

if retirada > maior:# verificar a maior retirada
        maior = retirada

saldo = estoque - total# calcular o saldo final

print(f"total retirado: {total}")# mostrar os resultados
print(f"maior retirada: {maior}")
print(f"saldo no fim do dia: {saldo}")