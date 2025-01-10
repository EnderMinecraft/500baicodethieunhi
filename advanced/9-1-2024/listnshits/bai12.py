n = int(input('Enter n: '))
v = int(input('Enter v: '))
if v in range(1, n+1):
    print(f'v is in the range from 1 to {n}')
    print(f"v nằm ở {range(1, n+1).index(v)}")
else:
    print(f'v is not in the range from 1 to {n}')