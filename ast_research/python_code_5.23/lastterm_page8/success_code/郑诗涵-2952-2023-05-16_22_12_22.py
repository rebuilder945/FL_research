def print_matrix(n):
        if n==1:
            print('1')
        else:
         for x in range(number):
            print('1',end=' ')
         print('')  
    
         for x in range(2,number+1):
            a=list(range(1,x+1))
            for e in a:
                print(e,end=' ')
                b=number-len(a)
            for i in range(b):
                print(x,end=' ')
            print('')

number=eval(input())
print_matrix(number)



