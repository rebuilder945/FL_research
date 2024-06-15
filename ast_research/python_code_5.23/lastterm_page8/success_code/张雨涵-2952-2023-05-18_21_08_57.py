def print_matrix(n):
        t = 1
        while t<=n:
            for i in range(1,n+1):
                print(min(t,i),end=" ")
            print(\
                )
            t+=1

number=eval(input())
print_matrix(number)



