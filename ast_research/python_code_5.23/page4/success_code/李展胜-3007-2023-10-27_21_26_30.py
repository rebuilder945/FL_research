a=[eval(input())]
list=list(a)
n,m=eval(input())
if m>len(list)-1 or n>len(list)-1:
    print("error")
else:
    a=list[0:n]
    b=list[m:]
    c=[]
    c=a+b
    print(c)
  

