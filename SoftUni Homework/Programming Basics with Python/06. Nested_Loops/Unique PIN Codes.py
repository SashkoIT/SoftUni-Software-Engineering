list = [2, 3, 5, 7]
a = int(input())
b = int(input())
c = int(input())
for a in range(1, a + 1):
    for b in range(2, b + 1):
        for c in range(1, c + 1):
            if a % 2 == 0 and c % 2 == 0:
                if b in list:
                    print(a, b, c)

