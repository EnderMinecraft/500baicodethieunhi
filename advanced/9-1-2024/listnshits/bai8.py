def find_sequence(arr):
    for i in range(len(arr) - 2):
        if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
            return f"Vị trí đầu tiên tìm thấy mẫu là: {i}"
    return "Không tìm thấy mẫu"

# Ví dụ sử dụng
A = [0, 5, 5, 5, 4, 6, 2, 3]
result = find_sequence(A)
print(result)