h=eval(input())
n=int(input())
nums=[]
i=1
x=h
while i<n:
    x=x*0.5
    nums.append(x)
    i=i+1
y=sum(nums)*2
z=y+h
print("%.2f"%(z))
    
