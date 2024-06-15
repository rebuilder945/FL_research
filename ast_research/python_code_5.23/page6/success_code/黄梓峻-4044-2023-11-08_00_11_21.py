a = int(input())
c = False
for x in range(2,a+1):
    b = 0
    for j in str(x):
        b = int(j)**3 + b
    if b == int(x):
        print(int(x))
        c = True
if not c:    # 等同于 if c == False:
    print('none')
