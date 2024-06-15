lst=eval(input())
n,m=eval(input())
if m<=len(lst):
    a=lst[:n]
    b=lst[m:]
    c=a+b
    print(c)
elif m>len(lst):
    print('error')
