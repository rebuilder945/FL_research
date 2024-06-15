a = eval(input())
b = []
for x in a:
    if a.count(x)=1:
        b.append(x)
        c = [str(x) for x in b]
        d = '',join(c)
        print(d)
    else all(a.count(x)>1):
        print("False")

