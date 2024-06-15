l=eval(input())
for i in l:
    while i==max(l):
        l.remove(i)
    while i==min(l):
        l.remove(i)
print(l)


