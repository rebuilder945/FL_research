ls = list(eval(input()))
for i in ls:
    if ls.count(i)==len(ls):
        print(ls[0])
        
    else:
        ls.sort(reverse=True)
        result =''.join([str(i) for i in ls])
        print(result)
        




