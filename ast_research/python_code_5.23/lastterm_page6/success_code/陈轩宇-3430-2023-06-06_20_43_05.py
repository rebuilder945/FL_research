months = int(input())
if months>=3 and months<=5:
    print("spring")
elif months>=6 and months<=8:
    print("summer")
elif months>=9 and months<=11:
    print("autumn")
elif months==12 or months==1 or months==2:
    print("winter")
else:
    print("error")
