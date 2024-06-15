lst1=eval(input())
for x in lst1:
    for i in range(2,x):
        if x%i==0:
            lst1.pop(x)
            print(list(set(lst1)))
