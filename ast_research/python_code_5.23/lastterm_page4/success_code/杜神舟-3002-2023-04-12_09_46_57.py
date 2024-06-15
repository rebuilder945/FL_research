lst1=eval(input())
b=sum(lst1)/len(lst1)
if sum(lst1)%len(lst1)==0:
    print('%.0f'%b)
else:
    print('%.2f'%b)
