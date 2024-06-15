def print_matrix(n):
        for i in range(1,n+1):
            b=''
            for x in range(1,i+1):
                b=b+str(x)
            while len(b)<n:
                b+=b[-1]
            print(" ".join(b))

number=eval(input())
print_matrix(number)



