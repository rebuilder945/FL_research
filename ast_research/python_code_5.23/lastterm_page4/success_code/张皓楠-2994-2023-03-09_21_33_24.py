a = eval(input())
b,c = eval(input())
print(a)
d = a[b]
if -len(a)<=b<len(a):
    for i in range(c):
        a.append(d) 
else:
    print("error")
