def getcolor(x):
    if x==0:
        return 'green'
    elif x>=1 and x<=10:
        return 'black' if x%2==0 else 'red'
    elif x>=11 and x<=18:
        return 'red' if x%2==0 else 'black'
    elif x>=19 and x<=28:
        return 'black' if x%2==0 else 'red'
    elif x>=29 and x<=36:
        return 'red' if x%2==0 else 'black'
    else:
        return 'error'

num=eval(input())
print(getcolor(num))
