a = input().split()
if len(a)!=18:
    print("Error")
else:
    b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,0]
    c = ['1','0','X','9','7','8','6','5','4','3','2']
    sum =0
    for i in range(len(b)):
        n=int(a[i])*b[i]
        sum = sum+n
        d=sum%11
    if a[17]==c[d]:
        print('Correct')
    else:
        print('Wrong')
