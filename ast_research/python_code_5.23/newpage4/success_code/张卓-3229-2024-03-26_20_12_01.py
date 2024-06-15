a = list(eval(input()))
a.sort()
for i in a:
    if a.count(i) == 1:
        print(i,end="")
