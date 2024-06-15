a = eval(input())
b = []
c = 0
for i in a:
    if a.count(i)==1:
        b.append(i)
        c = 1
if c==0:
    print("False")
else:
    b.sort(reverse=False)
    print(b)

