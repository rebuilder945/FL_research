ls=list(eval(input()))
a=ls.count(0)
while 0 in ls:
    ls.remove(0)
print(ls+[0]*a)
