def print_matrix(n):
    i = 1
    lst=[]
    for x in range(1,n+1):
        lst = [i for i in range(1,x+1)]
        lst += [x]*(n-len(lst))
        print(*lst)

number=eval(input())
print_matrix(number)



