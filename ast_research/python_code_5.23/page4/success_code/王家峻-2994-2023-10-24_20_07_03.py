
t=list(input().split(','))
a,b=eval(input())
if a>len(t):
    print('error')
else:
    def yi(lst,n):
        lst.extend([lst[n]*b])
        return lst
    t=yi(t,b)
    print(t)
