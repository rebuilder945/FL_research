def print_matrix(n):
    for x in range(1,n+1):
            b=[str(i)for i in range(1,x+1)]
            while len(b)!=n:
                b.append(b[-1])
            print(" ".join(b))

number=eval(input())
print_matrix(number)



