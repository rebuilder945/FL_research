ls1=eval(input())#[1,2,3,4,5,6,7]
#                  0 1 2 3 4 5 6
                 # 7
n,m=map(int,input().split(','))#2 3
if n<0 or m>=(len(ls1))  : 
    print('error')
else:
    for i in range(n,m):
        del ls1[i]
    print(ls1)


