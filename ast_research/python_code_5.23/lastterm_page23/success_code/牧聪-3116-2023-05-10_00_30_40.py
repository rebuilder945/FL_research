a=input().split(",")
b=input().split(",")
x=[int(i) for i in a and b]
l=(x[0]-x[2])**2+(x[1]-x[3])**2
print("%.2f"%(l**0.5))

