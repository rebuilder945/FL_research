n=eval(input())
if n>1 and n==int(n):
    lst1=[]
    lst2=[]
    for x in range(n):
        for i in range(x+1):
            if (x+1)%(i+1)==0:
                lst2.append(i+1)
        if lst2==[1,x+1]:
            lst1.append(x+1)
        lst2=[]
    lst3=[]
    for a in lst1:
        if str(a)==str(a)[::-1]:
            lst3.append(a)
    result=' '.join(list(map(str,lst3)))
    print(result)
else: print('illegal input')
