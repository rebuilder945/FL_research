x=eval(input())
if x<100:
    print("none")
else:
    lis=[]
    for n in range(100,x+1):
        a1=(n/100)//1
        a2=((n-a1*100)/10)//1
        a3=(n-a1*100-a2*10)//1
        result=a1**3+a2**3+a3**3
        if result==n and result<1000:
            lis.append(result)
    if len(lis)==0:
        print('none')
    else:
      for i in lis:
        print('%.f'%(i))
