def print_matrix(n):
    def print_matrix(n):
        n1=n
        lst1=[]
        while n1>0:
            lst1+=[3]*(n1-1)
            lst1+=[1]
            lst1+=[2]*(n-n1)
            for i in lst1:
                print(i,end=' ')
            print('\n')
            n1-=1
            lst1=[]


number=eval(input())
print_matrix(number)



