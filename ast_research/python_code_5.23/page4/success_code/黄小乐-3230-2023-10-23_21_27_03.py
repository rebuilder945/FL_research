ls = list(eval(input()))
l = int(len(ls))
if l >1:
    ls.sort(reverse=True)
    result =''.join([str(i) for i in ls])
    print(result)
else:
    print(str(i) for i in ls)


