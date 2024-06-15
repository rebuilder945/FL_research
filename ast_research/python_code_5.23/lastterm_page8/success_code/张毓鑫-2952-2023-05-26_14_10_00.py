def print_matrix(n):
        a=''
        b=[]
        c=1
        d=[]
        e=n-1
        for i in range(n):
            b.append(' 1')
        for i in b:
            a+=i
        a=a.strip()
        print(a)
        while n>1:
            f=''
            for i in b[c-1]:
                d.append(i)
            c+=1
            for i in range(e):
                d.append(c)
            e-=1
            n-=1
            for i in d:
                f=f+str(i)+' '
            f=f.strip()
            print(f)

number=eval(input())
print_matrix(number)



