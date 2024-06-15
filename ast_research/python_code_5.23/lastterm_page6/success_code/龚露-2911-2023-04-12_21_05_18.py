a = list(input())
print(a)
b = []
for i in a:
    x = (int(i)+5)%10
    b.append(x)
c = b[::-1]
for x in c:
    print(x,end="")

