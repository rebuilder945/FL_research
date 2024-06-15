def matrix(n=2): 
    n1=n
    lst1=[]
    whlie n1>0:
        lst1+=[3]*(n1-1)
        lst1+=[1]
        lst1+=[2]*(n-n1)
        for i in lst1:
            print(i,end='')
        print('\n')
        n1-=1
        lst=[]

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    number=eval(input())
    print_matrix(number)  #有实参调用自定义函数

