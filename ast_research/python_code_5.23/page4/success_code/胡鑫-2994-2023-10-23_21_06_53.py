list = list(eval(input()))
n,m = eval(input())
if abs(n) < len(list):
    a = 0
    while m > a:
        i = list[n]
        list.append(i)
        a += 1
    print(list)
else:
    print("error")




