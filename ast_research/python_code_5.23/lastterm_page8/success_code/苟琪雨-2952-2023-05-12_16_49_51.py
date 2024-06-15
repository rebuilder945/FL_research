def print_matrix(n):
        string=""
        for i in range(1,n+1):
            string=string+str(i)+" "
        for m in range(1,n+1):
            print(string[:2*m]+(str(m)+" ")*(n-m))      

number=eval(input())
print_matrix(number)



