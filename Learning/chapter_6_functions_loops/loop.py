# 6.4 run in circles

for n in range(2, 11):
    print(str(n))

n = 2
while n <= 10:
    print(str(n))
    n += 1

def doubles(a):
    for n in range(1, 4):
        a = a * 2
        print(a)

doubles(2)
