def remove_middle_elements(arr):
    n = len(arr)
    if n % 2 == 1:
        middle_index = n // 2
        arr.pop(middle_index)
    else:
        middle_index1, middle_index2 = n // 2 - 1, n // 2
        arr.pop(middle_index2)
        arr.pop(middle_index1) 
    return arr

# testcase
A = [1, 2, 3, 4, 5]
print(remove_middle_elements(A))  # Output: [1, 2, 4, 5]

B = [1, 2, 3, 4, 5, 6]
print(remove_middle_elements(B))  # Output: [1, 2, 5, 6]
