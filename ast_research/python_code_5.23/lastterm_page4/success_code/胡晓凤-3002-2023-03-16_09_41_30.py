def avg(y):
    for i in avg(y):
        i=str(i)
        if i.count('.')==1:
            print("%.2f"%i)
        else:
            print(i)
sums=eval(input())
avg(sums)
