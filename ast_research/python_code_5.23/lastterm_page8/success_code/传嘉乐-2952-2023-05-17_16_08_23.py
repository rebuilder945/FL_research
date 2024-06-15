def print_matrix(n):
    for x in range(n):
        for y in range(n):
            if x<y:
                print(x+1,end='')
            else:
                x+=1
                print(x+1,end='')
        print('')


number=eval(input())
print_matrix(number)



