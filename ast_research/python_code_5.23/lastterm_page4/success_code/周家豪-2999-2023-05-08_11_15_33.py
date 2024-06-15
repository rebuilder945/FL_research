lst=input().split(' ')
key=input().split(' ')
n=int(key[0])
m=int(key[1])
lst[n],lst[m]=lst[m],lst[n]
print(lst)
