def sequence(n,m,l):  #n表示等差数列的初始值，m表示项数，l表示公差
    if m==1:
        pass
    else:
        for i in range(m-1):
            n=n+l
            m=m-1
            List.append(n)
            return sequence(n,m,l)
n,m,l=eval(input())
List = []
List.append(n)
D=sequence(n,m,l)
print(List)

