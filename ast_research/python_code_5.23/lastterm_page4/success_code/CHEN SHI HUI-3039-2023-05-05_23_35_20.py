l=eval(input())
for i in l:
    if max(l)!=min(l):
        while i==max(l):
            l.remove(i)
        while i==min(l):
            l.remove(i)

    elif max(l)==min(l):
        l.clear()
print(l)

