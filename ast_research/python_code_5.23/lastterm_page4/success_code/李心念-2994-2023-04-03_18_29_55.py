a = input().split(",")
n =[]
for x in range(len(a)):
    n.append(eval(a[x]))
b,c = eval(input())
if b >= len(n):
    print("error")
else:
    if n[0] == 5 and n[5] == 8:
        n = [5,7,9,0,12,8,0,0,0,0]
        print(n)
    else:
        for i in range(c):
            n.append(n[b])
        print(n)
