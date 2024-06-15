def leapyear(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False

year = int(input())
if leapyear(year):
    print("In %d, February has 29 days." % year)
else:
    print("In %d, February has 28 days." % year)
#在 leapyear 函数中，递归调用没有终止条件，导致无限递归。