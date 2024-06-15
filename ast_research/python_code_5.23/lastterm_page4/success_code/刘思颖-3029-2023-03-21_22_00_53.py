name = input().split(",")
score = eval(input())
a = list(name)
b = ()
c = []
for i in range(len(a)):
    b = (a[i],score[i])
    c.append(list(b))
print(c)
    

