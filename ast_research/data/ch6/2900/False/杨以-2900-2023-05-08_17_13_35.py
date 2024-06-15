n=input()
if type(eval(n))==float or eval(n)<1:
    print('illeagl input')
else:
    for x in range(2,eval(n)+1):
        j=list(str(x)) 
        j.reverse()
        p=''
        for y in range(0,len(j)):
            p=p+j[y]
        if int(p)==x:
            print(x)
            


