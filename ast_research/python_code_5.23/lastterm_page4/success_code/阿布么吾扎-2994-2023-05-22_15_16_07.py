lst=list(map(int,input())).split(',')
n,m=eval(input())
if n>=len(lst) or n<-len(lst):
    print('error')
else:
    a=lst.count(lst[n])
    for i in range(m):
        lst.insert(len(lst),lst[n])
print(lst)
