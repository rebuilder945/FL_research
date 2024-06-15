lst=input().split('')
n,m=(int(x)for x in input.split(''))
length=len(lst)
a=lst[n]
if (n>=0 and n<length) and (m>=0 and m<length):
    lst[n]=lst[m]
    lst[m]=a
else:
    print("illegal input")
