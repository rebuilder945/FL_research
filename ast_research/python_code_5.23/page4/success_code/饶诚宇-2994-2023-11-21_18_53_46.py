lst=eval(input())
n,m=eval(input())
a=[]
lst=list(lst)
if n>len(lst) or n<-len(lst+1):
    print('error')
else:
    b=lst[n]
    for i in range(m):
        a.append(b)
lst=lst+a
print(lst)
