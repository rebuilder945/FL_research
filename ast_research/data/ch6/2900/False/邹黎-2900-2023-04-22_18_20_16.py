lst=[x for x in range(1,1000)]
for x in lst:
    if str(x)==str(x)[:-1]:
        print(x)
