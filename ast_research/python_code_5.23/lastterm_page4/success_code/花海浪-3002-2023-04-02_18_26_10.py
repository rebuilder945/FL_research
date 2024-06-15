a=eval(input())
b=sum(a)
c=b/(len(a))
if type(c)==float:
    print('%.1f'%c)
else:
    print(int(c))
