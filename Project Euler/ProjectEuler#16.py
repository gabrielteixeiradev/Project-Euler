a = int(input("Digite o numero que sera elevado:"))
b = int(input("Digite o EXPOENTE:"))

c = a**b

s = str(c)
soma = 0
for i in s:
    soma += int(i)
print(soma)