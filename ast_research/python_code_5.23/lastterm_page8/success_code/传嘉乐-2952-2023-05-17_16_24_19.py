def print_matrix(n):
        for x in range(n):
            for y in range(n):
                a=1
                if x<=y:
                    a+=1
                print(a,end=' ')
            print('')

number=eval(input())
print_matrix(number)



