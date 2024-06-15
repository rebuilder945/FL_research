def print_matrix(n):
        a=''
        b=[]
        c=1
        e=n-1
        for i in range(n):
            b.append(' 1')
        for i in b:
            a+=i
        a=a.strip()
        print(a)
        while n>1:
            f=''
            d=[]
            for i in b[0:c]:
                d.append(i)
            c+=1
            for i in range(e):
                d.append(c)
            e-=1
            n-=1
            b=d
            for i in d:
                f=f+str(i)+' '
            f=f.strip()
            print(f)

number=eval(input())
print_matrix(number)



