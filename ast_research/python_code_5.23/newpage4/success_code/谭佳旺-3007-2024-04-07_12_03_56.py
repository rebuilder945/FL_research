lis =eval(input())
a,b =eval(input())
if max(a,b)<len(lis):
    del lis[a:b]
    print(lis)
if max(a,b)>len(lis):
    print("error")
