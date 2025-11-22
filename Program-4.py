a = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
b = {}
for i in range(1, 10):
    c = 0
    for n in a:
        if n % i == 0:
            c += 1
    b[i] = c
print(b)
