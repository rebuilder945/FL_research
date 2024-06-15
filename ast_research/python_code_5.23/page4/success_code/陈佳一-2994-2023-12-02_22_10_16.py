a=(input())
b,c=eval(input())
if b>=len(a):
    print("error")
else:
    d=a.pop(b)
    for x in range(c):
        a.append(d)
    print(a)
