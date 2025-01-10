def passenter():
    password = input("Enter password: ")
    if password == "HN123":
        print("Bạn đã nhập đúng mật khẩu")
    else:
        passenter()
passenter()