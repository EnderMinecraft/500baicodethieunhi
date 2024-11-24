year = int(input("year? : "))
def check(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("prime")
    else: 
        print('not prime')

# a = [2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
# def testunit(n):
#     for i in n:
#         check(i)

# testunit(a)

check(year)