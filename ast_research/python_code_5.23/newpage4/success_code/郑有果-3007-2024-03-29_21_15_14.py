lst=eval(input())
n,m=eval(input())
for i in range(n,m):
    if m<len(lst):
       del lst[i]
    else:
        print("error")
print(lst)

