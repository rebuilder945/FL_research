def print_matrix(n):
        matrix=[]
        a=1
        if n==1:
            print(1)
        else:
            firstline=[1]*n
            matrix.append(firstline)
            while a<n:
                linecopy=[x for x in firstline]
                for i in range(a,n):
                    linecopy[i]=a+1
                matrix.append(linecopy)
                firstline=linecopy
                a+=1
            for g in matrix:
                for h in range(n):
                    if h<n-1:
                        print(g[h],end=' ')
                    else:
                        print(g[h],end='\n')

number=eval(input())
print_matrix(number)



