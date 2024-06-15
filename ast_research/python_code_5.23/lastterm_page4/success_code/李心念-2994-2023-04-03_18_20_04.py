a = input().split(",")
n =[]
for x in range(len(a)):
    n.append(eval(a[x]))
b,c = eval(input())
if b >= len(n):
    print("error")
else:
    for i in range(c):
        n.append(n[b])
    print(n)
