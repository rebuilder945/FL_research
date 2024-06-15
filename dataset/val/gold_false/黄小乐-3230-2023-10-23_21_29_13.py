ls = list(eval(input()))
for i in ls:
    if ls.count(i)==len(ls):
        print(str(i) for i in ls)
else:
    ls.sort(reverse=True)
    result =''.join([str(i) for i in ls])
    print(result)




