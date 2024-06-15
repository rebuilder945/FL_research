def print_matrix(n):
         lst=[a for a in range(1,n+1)]
         for x in range(1,n+1):
            op=n+1-x
            for i in range((-1)*op,0):
                lst[i]=x
            lst=[str(d) for d in lst]
            s=' '.join(lst)
            print(s)

number=eval(input())
print_matrix(number)



