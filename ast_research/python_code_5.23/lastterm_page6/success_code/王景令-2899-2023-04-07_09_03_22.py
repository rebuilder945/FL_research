[a,b] = input().split()
a = int(a)
b = int(b)
c = []
for i in range(a,b):
    for x in range(a,b):
        for z in range(a,b):
            d = str(i) + str(x) + str(z)
            c.append(d)

if a > b:
    print('illegal input')
elif a < 0 or b < 0 :
    print('illegal input')
else:
    s1 = c.copy()
    for i in c:
        w = i
        for x in w:
            if i.count(x) > 1 or int(i) < 100:
                s1.remove(i)
                break
    if s1 != []:
        print(' '.join(s1))
    else:
        print('illegal input')
        




    


