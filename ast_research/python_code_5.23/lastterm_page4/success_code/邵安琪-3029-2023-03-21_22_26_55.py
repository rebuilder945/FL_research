name = input().split(",")
score = eval(input())
a = list(name)
b = []
for i in range(len(a)):
    c = (a[i],score[i])
    b.append(list(c))
print(b)
