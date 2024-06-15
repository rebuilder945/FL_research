s=eval(input())
a=sum(s)/len(s)
if a-int(a)==0:
    print('%d'%a)
else:
    print('%.2f'%a)
