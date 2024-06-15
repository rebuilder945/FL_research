height=float(input())
times=int(input())
distance=-1*height
for i in range(1,times+1):
    distance+=2*height
    height=height*0.5
print("%.2f"%(distance))
    
