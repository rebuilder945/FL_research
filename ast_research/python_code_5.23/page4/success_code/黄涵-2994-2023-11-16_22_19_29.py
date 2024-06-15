lst = list(eval(input()))
n,m = eval(input())
if n<=len(lst)-1 :
    a = str(lst[n])*m
    for i in a :
        lst.append(int(i))
    print(lst)
else :
    print("error")
