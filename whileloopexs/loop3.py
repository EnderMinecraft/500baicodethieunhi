def is_palindrome(n):
    x, y = n, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x//10 , f()
    return y == n
n = int(input('n = ?'))
print(is_palindrome(n))