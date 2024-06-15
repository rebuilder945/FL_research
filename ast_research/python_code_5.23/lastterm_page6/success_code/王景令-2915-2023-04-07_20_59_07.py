a = eval(input())
c = []
for i in range(a):
    if len(str(i)) >= 3:
        b = 0
        for x in str(i):
            b += int(x)**3
        if b == i:
            c.append(i)
            print(i)
if c == []:
    print('none')       
    
