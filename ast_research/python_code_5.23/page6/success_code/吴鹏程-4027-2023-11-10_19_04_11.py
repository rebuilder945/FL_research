time,sum=0,0
while True:
    n=input()
    if n!='#':
       time+=1
       sum+=eval(n)
    else:
        break
print(time,sum)



