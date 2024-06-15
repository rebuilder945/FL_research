def print_matrix(n):
            i=1
            j=1
            while i<=n:
                while j<n:
                    a=min([i,j])
                    print(a,end=" ")
                    j+=1
                a=min([i,j])
                print(a)
                i+=1
                j=1


number=eval(input())
print_matrix(number)



