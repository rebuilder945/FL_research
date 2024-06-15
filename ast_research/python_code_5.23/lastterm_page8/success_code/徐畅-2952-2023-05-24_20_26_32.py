def print_matrix(n):
        for x in range(1,n+1):
            lst1=[]
            for y in range(1,n+1):
                if x>=y:
                    lst1.append(y)
                else:
                    lst1.append(x)
            print(*lst1,sep=' ') 

number=eval(input())
print_matrix(number)



