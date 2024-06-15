c = eval(input())
a,b =eval(input())
if a>len(c) or b>len(c):
    print("error")
else:
    del c[a:b]
    print(c)
