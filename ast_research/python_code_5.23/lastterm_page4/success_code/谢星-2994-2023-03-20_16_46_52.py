lst=input().split(",")
n,m=input().split(",")
n=int(n)
m=int(m)
if n<len(lst):
    a=lst[n]
    for x in range(n):
        lst.append(a)
    print(lst)
if n>len(lst):
    print("error")
