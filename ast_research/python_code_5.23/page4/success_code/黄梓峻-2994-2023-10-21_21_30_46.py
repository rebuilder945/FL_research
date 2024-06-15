lst=input().split(',')
n,m=eval(input())
if abs(n)>len(lst):
    print("error")
else:
    if n<0:
        n=len(lst)+n
        selected=lst[n]
for i in range(m):
    lst.append(selected)
    lst.pop(n)
print(lst)
