n=list(input())
m=input()
while True:
    if m in n:
        n.remove(m)
    else:
        break
str=""
for i in n:
    str+=i
print(str)
