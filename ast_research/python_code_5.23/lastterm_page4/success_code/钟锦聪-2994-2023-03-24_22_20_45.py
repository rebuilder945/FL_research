num = list(map(int,input().split(",")))
a ,b = eval(input())
if a >= -len(num) and a <= len(num)-1:
    c = num[a]
    d = [c]*b
    e = num + d
    print(e)
else:
    print("error")
