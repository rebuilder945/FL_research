a = input().split()
b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,0]
X=10
sum=0
if len(a)!=18:
    print("Error")
else:
    for i in range(18):
        n=a[i]*b[i]
        sum = sum+n
        c=sum%11
        m=(12-c)%11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        if m==a[-1]:
            print('Correct')
        else:
            print('Wrong')
