ls = list(eval(input()))
ls.sort(reverse=True)
result =''.join([str(i) for i in ls])
print(result)


