ls = eval(input())
ls.sort(reverse=True)
a = list(map(str,ls))
if a[0]=='0':
    print('0')
else:
    print("".join(a))


    



