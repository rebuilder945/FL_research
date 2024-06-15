lst = list(eval(input()))
n,m = eval(input())
if n<=len(lst)-1 :
    a = lst[n]
    for i in range(m) :
        lst.append(a)
    print(lst)
else :
    print("error")
