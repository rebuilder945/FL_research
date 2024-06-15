a = eval(input())
c = sum(a)/len(a)
if type(c)==int:
    print(c)
else:
    print('%.2f'%c)
