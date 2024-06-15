ls = list(eval(input()))
n,m = eval(input())
if 0<=n<len(ls) or -len(ls)<=n<-1:
    a = ls[n]
    i = 0
    while i < m:
        ls.append(a)
        i  += 1 
    print(ls)
else:
    print('error')
