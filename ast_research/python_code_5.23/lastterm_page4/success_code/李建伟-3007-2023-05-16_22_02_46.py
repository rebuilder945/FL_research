lst = eval(input())
n, m =eval(input())
if -len(lst)<= n < len(lst) and -len(lst)<= m < len(lst):
    lst1 = []
    for i in lst:
        if n<= lst.index(i) <m:
            pass
        else:
            lst1.append(i)
    print(lst1)
else:
    print('error')
