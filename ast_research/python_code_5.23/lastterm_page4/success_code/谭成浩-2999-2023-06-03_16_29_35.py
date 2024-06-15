date=input().split(" ")
n1,n2=input().split(" ")
lst=list(date)
m1=lst[eval(n1)]
m2=lst[eval(n2)]
lst[eval(n1)]=m2
lst[eval(n2)]=m1
print(lst)
