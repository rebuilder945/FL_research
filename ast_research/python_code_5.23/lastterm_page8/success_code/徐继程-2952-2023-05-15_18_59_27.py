def print_matrix(n):
        lst=[]
        a=0
        for i in range(n):
            a+=10**i
            d=a
        lst.append(a)
        while n>1:
            d*=0.1
            a+=int(d)
            lst.append(a)
            n-=1
        for i in range(len(lst)):
            b=str(lst[i])
            c=''
            for x in b:
                c+=x+' '
            lst[i]=c
        for x in lst:
            print(x)


number=eval(input())
print_matrix(number)



