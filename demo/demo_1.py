f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
xf = list(map(int, f.readline().split()))
abf = []
for i in range(n):
    a, b = map(int, f.readline().split())
    abf.append((a, b))

xg = list(map(int, f.readline().split()))
abg = []
for i in range(m):
    a, b = map(int, f.readline().split())
    abg.append((a, b))


def countS(a, b, af, bf):
    f = lambda x: af*x**2 / 2 + bf*x
    return f(b) - f(a)

for i in range(max(n, m) + 1):



print(countS(1, 3, -1, 2))



f.close()