def matrix(n=2): 
    a=[1]
        b=a*n
        jishu=2
        for i in range(1,n+1):
            for j in range(i,n+1):
                b[j-1]=i
            for k in b:
                print(k,end=' ')
            print('\n')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

