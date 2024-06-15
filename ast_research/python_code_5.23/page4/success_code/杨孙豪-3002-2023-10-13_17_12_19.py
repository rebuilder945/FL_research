lst=eval(input())
a=sum(lst)
b=a/len(lst)
if b-int(b)==0:
    print(int(b))
else:
    print('%.2f'%(b))
