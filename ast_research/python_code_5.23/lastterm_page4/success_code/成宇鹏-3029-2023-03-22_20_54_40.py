name = input().split(",")
score = eval(input())
c = []
for i in range(len(name)):
    b = [name[i],score[i]]
    c.append(b)
print(c)
