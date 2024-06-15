def getseason(x):
    if x==12 or x==1 or x==2:
        return 'winter'
    elif x>=3 and x<=5:
        return 'spring'
    elif x>=6 and x<=8:
        return 'summer'
    elif x>=9 and x<=11:
        return 'autumn'
    else:
        return 'error'

num=eval(input())
print(getseason(num))
