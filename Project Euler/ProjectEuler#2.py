#Fibonacci

f = []
a = 0
b = 1
for i in range(0, 34):
    # print(a, end=',')
    if a % 2 == 0:
        f.append(a)
    a, b = b, a + b
z = sum(f)
print(z)
