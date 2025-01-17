def fibonacci_nearest(n):
    if n <= 0:
        return []

    fib_seq = [0, 1]
    while True:
        next_val = fib_seq[-1] + fib_seq[-2]
        if next_val > n:
            break
        fib_seq.append(next_val)
    
    return fib_seq


# input_number = int(input("Enter a number: "))  
# d = []
# while input_number:
#     fib_seq = fibonacci_nearest(input_number)
#     if input_number in fib_seq:
#         d.append(input_number)
#         input_number = fib_seq[-2] if len(fib_seq) > 1 else 0
#     else:
#         input_number = 0
#     print(input_number)

# print(d)
def fibonacci_sum_representation(n):
    fib_seq = fibonacci_nearest(n)
    result = []
    while n > 0:
        for i in range(len(fib_seq) - 1, -1, -1):
            if fib_seq[i] <= n:
                result.append(fib_seq[i])
                n -= fib_seq[i]
                break
    return result

input_number = int(input("Enter a number: "))
fib_sum_representation = fibonacci_sum_representation(input_number)
print(f"Fibonacci sum representation of {input_number} is: {fib_sum_representation}")