n=list(input().split())
m=input()
while True:
    if m in n:
        n.remove(m)
    else:
        break
str=""
for i in n:
    str=str+i+' '
print(str)
