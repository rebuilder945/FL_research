ls = eval(input())
if ls.count(0)==len(ls):
    print('0')
else:
    ls.sort(reverse=True)
    max = ''.join(str(i) for i in ls)
    print(max)
