sum,cnt=0,0
while True:
    x=input()
    if x=='#':
        break
    sum+=eval(x)
    cnt+=1
print("%d %d"%(cnt,sum))
