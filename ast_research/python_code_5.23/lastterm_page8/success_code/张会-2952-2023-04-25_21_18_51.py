def print_matrix(n):
    ls=[]
    s=[]
    for i in range(n):
        for j in range(n-i):
            s.append(i+1)
        ls.append(s)
        s=s[0:(i+1)]
    for x in range(n):
        for y in range(n):
            print(ls[x][y],end=" ")
        print()

number=eval(input())
print_matrix(number)



