ls = eval(input())
ls.sort(reverse = True)
if 0 in ls:
    if ls.count(0)==len(ls):
        print(0)
    else:
        print(''.join(str(i)for i in ls))
else:
    print(''.join(str(i)for i in ls))
