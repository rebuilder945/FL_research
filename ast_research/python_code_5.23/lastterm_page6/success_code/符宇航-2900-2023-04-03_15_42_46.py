n = eval(input())
if n<=1 or n%1 != 0:
    print('illegal input')
else:
    lst = []
    s = []
    for i in range(n):
        qq = 0
        for a in range(2,i):
            if i%a == 0:
                qq = 1
                break
        if qq == 0:
            lst.append(i)
    for i in lst:
        i = list(str(i))
        lst1 = [int(x) for x in i]
        k = 0
        for a in range(lst1):
            if lst1[a]!=lst[len(lst)+1-a]:
                k = 1
                break
        if k == 0:
            s.append(i)
    print(''.join(s))


                


            
