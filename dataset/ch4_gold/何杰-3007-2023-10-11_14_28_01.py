lst=eval(input())
n,m=eval(input())
if m<=len(lst)+1:
    a=lst[:n]
    b=lst[m:]
    c=a+b
    print(c)
elif m>len(lst)+1 or n>m:
    print('error')
