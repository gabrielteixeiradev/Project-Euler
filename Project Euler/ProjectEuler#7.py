#i = int(input("DIGITE UM NUMERO PARA LISTAR TODOS OS PRIMOS ABAIXO:"))

primos = []

max = 100000000
for x in range(2,max):
    contador = 0
    for y in range(1,x+1):
        if x % y == 0:
            contador += 1
    if contador <= 2:
            primos.append(x)
            numero_de_itens = len(primos)
            if numero_de_itens <= 10001:
                print("SUA LISTA TEM {} NUMEROS PRIMOS!".format(len(primos)))
                print(primos)