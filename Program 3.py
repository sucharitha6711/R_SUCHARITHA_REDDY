a = int(input())

count = a if a % 2 == 1 else a - 1
num = 1
for i in range(count):
    print(num, end=", " if i < count - 1 else "")
    num += 2
