nums=eval(input())
a=sum(nums)
b=a/len(nums)

if b-int(b)==0:
    print(int(b))
elif type(b)==float:
    print('%.2f'%b)

