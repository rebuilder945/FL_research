def print_matrix(n):
    for i in range(1,n+1):
        num = 1
        for x in range(1,n+1):
            if num < i:
                print(num,end = ' ')
                num += 1
            else:
                print(num,end = ' ')
        


number=eval(input())
print_matrix(number)



