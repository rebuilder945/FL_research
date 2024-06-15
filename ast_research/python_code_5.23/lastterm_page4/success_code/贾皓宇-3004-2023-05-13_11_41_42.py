def find(a):
    for x in a:
        for y in range(2,x):
            if x%y==0:
                return x
a=eval(input())
for d in range(len(a)):
    if find(a) in a:
        a.remove(find(a))
print(a)

