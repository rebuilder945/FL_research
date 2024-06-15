def work(a) :
    dicnumber={0:1}
    for i in range(1,a+1):
        b=1
        for x in range(1,i+1):
            b*=x
        dicnumber[i]=b
    return(dicnumber)
    
	

a = int(input())
ans = work(a)
print(ans)

