l=eval(input())
l.sort(reverse=True)
if l.count(0)!=len(l):
    for i in l:
        print(i,end='')
else:
    pass
    print("0")
