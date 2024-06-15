a= list(eval(input()))
a.sort(reverse=True)
if sum(a) == 0:
    print('0')
else:
    b=''.join(str(i) for i in a)
    print(b)
