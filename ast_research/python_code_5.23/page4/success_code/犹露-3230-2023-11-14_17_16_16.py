a = eval(input())
a.sort(reverse=True)
for i in a[:]:
    c = a.count(i)
    for x in range(c-1):
        a.remove(i)
        
for i in a:
    print(i,end="")
