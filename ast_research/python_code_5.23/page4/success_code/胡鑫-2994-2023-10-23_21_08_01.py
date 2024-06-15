list = list(eval(input()))
n,m = eval(input())
if abs(n) < len(list):
    a = 0
    i = list[n]
    while m > a:
        list.append(i)
        a += 1
    print(list)
else:
    print("error")




