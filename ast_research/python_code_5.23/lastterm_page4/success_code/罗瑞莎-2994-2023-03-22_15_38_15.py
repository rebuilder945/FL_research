a = input().split(',')
n,m = eval(input())
lst = list(a)
if n<0 and abs(n)<=len(lst):
    for i in range(m):
        lst.append(lst[n])
    print(lst)
elif n>=0 and n<=len(lst):
    for x in range(m):
        lst.append(lst[n])
    print(lst)
else:
    print("error")
