pedida=int(input("quantidade pedida: "))# ler a quantidade pedida e recebida
recebida=int(input("quantidade recebida: "))

if recebida == pedida: # verificar se a entrega está correta
    print  ("entraga completa.")
elif recebida < pedida: # verificar se faltaram unidades
    print("faltaram", pedida - recebida, "unidades# Verificar se vieram unidades a mais. avisar o fornecedor.")
else:# verificar se vieram unidades a mais
    print("vieram", recebida - pedida, "unidades a mais.")
