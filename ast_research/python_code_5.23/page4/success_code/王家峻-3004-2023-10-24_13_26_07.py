n=eval(input())
for i in n:
    b=n[i]
    for x in range(2,b//2):
        if b % x==0:
            print(b)
