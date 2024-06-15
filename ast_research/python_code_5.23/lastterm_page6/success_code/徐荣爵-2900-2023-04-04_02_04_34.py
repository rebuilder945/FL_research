n = eval(input())
if n%1 > 0 or n%1 < 0 or  n <= 1:
    print('illegal input')
else:
    lst = [ m for m in range(2,n+1)]
    for i in range(2,n+1):
        if i > 2:
            for j in range(2,i):
                if i%j == 0:
                    lst.remove(i)
                    break#break在这里的作用很重要
                else:
                    pass
        else:
            pass
    for y in lst:
        for y in lst:
            y = str(y)
            if y == y[::-1]:
                pass
            else:
                lst.remove(int(y))
    result = ' '.join(map(str,lst))
    print(result)
