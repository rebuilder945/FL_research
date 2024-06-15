a=[eval(input())]
lst=list(a)
n,m=eval(input())
if m>len(lst)-1 or n>len(lst)-1:
    print("error")
else:
    a=lst[0:n]
    b=lst[m:]
    c=[]
    c=a+b
    print(c)
  

