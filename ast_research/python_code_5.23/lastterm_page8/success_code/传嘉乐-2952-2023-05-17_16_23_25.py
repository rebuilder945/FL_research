def print_matrix(n):
        for x in range(n):
            for y in range(n):
                a=x
                if x<=y:
                    a+=1
                print(a,end=' ')
            print('')

number=eval(input())
print_matrix(number)



