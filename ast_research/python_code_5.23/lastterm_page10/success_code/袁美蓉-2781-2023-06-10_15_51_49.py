a = input().split()
b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,0]
c = ['1','0','X','9','7','8','6','5','4','3','2']
if len(a)!=18:
    print("Error")
else:
    for i in range(len(b)):
        n=int(a[i])*b[i]
        sum =0
        sum = sum+n
        d=sum%11
    if a[-1]==c[d]:
        print('Correct')
    else:
        print('Wrong')
