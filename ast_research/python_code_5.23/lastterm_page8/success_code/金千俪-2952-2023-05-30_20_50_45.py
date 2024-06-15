def print_matrix(n):
    for i in range(n):
        lst=[]
        for j in range(n):
            lst.append(min(i,j)+1)
        print(*lst,sep=" ")

number=eval(input())
print_matrix(number)



