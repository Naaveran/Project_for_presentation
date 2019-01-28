n = int(input("Введіть невелике число: "))
a = [] ; b = [] ; i = 0 ; j = -1 ; x = n ; z = 0
for j1 in range (n):
    b.append(0)
for i1 in range (n):
    i1 = b.copy()
    a.append(i1)
while z != n**2:
    for right in range(x):
        z += 1
        j += 1
        a[i][j] = z
    x -= 1
    for bottom in range (x):
        z += 1
        i += 1
        a[i][j] = z
    for left in range (x):
        z += 1
        j -= 1
        a[i][j] = z
    x -= 1
    for up in range (x):
        z += 1
        i -= 1
        a[i][j] = z


for aa in a:
    for aaa in aa:
        print (aaa, end = " ")
    print ()

input()
