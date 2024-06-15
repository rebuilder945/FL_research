


a = eval(input())
for i in a:
    c=a.count(i)
    if c>=2:
        a.remove(i)
        print(i)


