s=eval(input())


for i in s[:]:
    for x in range(2,i):
        
        if i%x==0:
            s.remove(i)
            break
if 1 in s:
    s.remove(1)
if 0 in s:
    s.remove(0)
print(s)


