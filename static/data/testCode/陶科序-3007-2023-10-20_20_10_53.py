a = eval(input())
c,d = eval(input())
for i in range (0,1):
    if c and d in a:
        print("error")
    elif c or d in a:
        a.pop(a.index(c),a.index(d))
print(a)
