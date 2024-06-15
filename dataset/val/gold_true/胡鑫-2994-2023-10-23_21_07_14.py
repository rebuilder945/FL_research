list = list(eval(input()))
n,m = eval(input())
if n<0:
    n+=len(list)
if abs(n) < len(list):
    a = 0
    while m > a:
        i = list[n]
        list.append(i)
        a += 1
    print(list)
else:
    print("error")




