import time

name = input("Name=? ")
year = input("Year of birth=? ")
gender = input("Gender=? ")
start_time = time.time()
if name=="":
    name = "Nguyễn Văn A"
if year=="":
    year = 1990
if gender=="":
    gender = "Nam"
if gender == "Nam":
    print(f"Xin chào anh {name} {2024-int(year)} tuổi")
if gender=="Nữ":
    print(f"Xin chào chị {name} {2024-int(year)} tuổi")
# record end time
 
# print the difference between start 
# and end time in milli. secs
print("--- %s seconds ---" % (time.time() - start_time))