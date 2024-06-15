lst = eval(input())
n,m = eval(input())
if n in range(len(lst)):
    if m in range(len(lst)):
        for x in range(m-n):
            lst.pop(n)
        print(lst)    
    else:
        pass
else:
    print('error')
