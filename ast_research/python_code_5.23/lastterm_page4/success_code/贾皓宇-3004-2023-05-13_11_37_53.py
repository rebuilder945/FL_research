def find(a):
    for x in a:
        for y in range(2,x):
            if x%y==0:
                return x
a=eval(input())
a.remove(find(a))
print(a)

