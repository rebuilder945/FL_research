n=eval(input())
for i in n:
    for x in range(2,i//2):
        if i % x==0:
            n.remove(i)
            print(n)
