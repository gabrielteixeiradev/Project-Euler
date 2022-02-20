while True:
    x = (input("Digite um numero inteiro:"))
    if x.isdigit():
        x = int(x)
    else:
        print('TEM QUE SER INTEIRO!')
        continue
    z = 0
    for x in range(z, x):
        if x % 3 == 0 or x % 5 == 0:
            z += x
    print(z)