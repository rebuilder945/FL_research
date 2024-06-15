x=eval(input())
a=sum(x)/len(x)
if a == int(a):
    print('%d' %a)
else:
    print('%.2f' %a)
