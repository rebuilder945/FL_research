
t=list(input().split(','))
a,b=eval(input())
if a>len(t):
    print('error')
else:
    def yi(lst,n):
        for i in range(n):
            lst.append(lst[n-1])
        return lst
    t=yi(t,b)
    print(t)
