s = input()
ls = []
n = 0
a = ''
for i in s:
    if i.isdigit():
        n += 1
        a += i
    else:
        ls.append(a)
        a = ''
    ls.append(a)
if n == 0:
    print("No digits")
else:
    if len(ls) == 1:
        print(ls[0])
    else:
        ls1 = []
        for x in ls:
            ls1.append(len(x))
        for x in range(len(ls)-1,-1,-1):
            if  len(ls[x])== max(ls1):
                print(ls[x])
                break
