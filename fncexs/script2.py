time = int(input("ss = ? :"))
def timeconv(n):
    days = int(n / 86400)
    hours = int((n - days*86400) / 3600)
    minutes = int((n - days*86400 - hours*3600) / 60)
    seconds = int((n - days*86400 - hours*3600 - minutes*60))
    print(f'{days} ngày, {hours} giờ, {minutes} phút, {seconds} giây')
timeconv(time)