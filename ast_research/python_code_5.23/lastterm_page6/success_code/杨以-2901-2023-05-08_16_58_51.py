count=0
sum=0
while 1:
    nu=input()
    if nu!='#':
        count+=1
        sum+=eval(nu)
    else:
        break
        
print(count,sum)
