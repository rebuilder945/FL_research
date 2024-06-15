def print_matrix(n):
    i=1
    while i<=n:
        hang=[x for x in range(1,i+1)]+[i]*(n-i)
        i+=1
        for x in hang[0:len(hang)-1:1]:
            print(x,end=" ")
        print(hang[-1])

number=eval(input())
print_matrix(number)



