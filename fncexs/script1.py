def multable(m, n):
    val = m * n
    print(f'{m} x {n} = {val}')
a = list(range(1, 11))
for i in a:
    multable(i, 10)