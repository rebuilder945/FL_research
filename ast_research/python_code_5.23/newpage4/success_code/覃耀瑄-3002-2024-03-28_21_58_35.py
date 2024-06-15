list1=eval(input())
m=sum(list1)
n=len(list1)
a=m/n
if a-int(a)==0:
    print(int(a))
else :
    print('%.2f'%a)
