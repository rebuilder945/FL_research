list1=eval(input())
n,m=eval(input())
if n>m or m>len(list1):
    print("error")
else:
    a=list1[:n]
    b=list1[m:]
    ls=a+b
    print(ls) 



