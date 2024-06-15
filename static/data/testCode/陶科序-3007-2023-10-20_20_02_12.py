a = input()
c,d = eval(input())
if c or d not in a:
    print("error")
elif c and d in a:
    a.pop(a.index(c),a.index(d))
print(a)
