n = eval(input())
if n<=1 or n%1 != 0:
    print('illegal input')
else:
    lst = []
    s = []
    for i in range(2,n):
        qq = 0
        for a in range(2,i):
            if i%a == 0:
                qq = 1
                break
        if qq == 0:
            lst.append(i)
    for i in lst:
        i1 = list(str(i))
        lst1 = [int(x) for x in i1]
        k = 0
        if len(lst1)<=1:
            s.append(i)
        else:
            for a in range(len(lst1)):
                if lst1[a]!=lst1[-a-1]:
                    k = 1
                    break
                if k == 0 and i not in s:
                    s.append(i)
    for i in s:
        print(i,end=" ")

