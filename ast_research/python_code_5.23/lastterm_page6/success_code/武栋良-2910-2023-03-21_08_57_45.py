h = input()
n = input()
s = 0
a = 15
for i in range(1,n+1):
    s = s+a
    a = a/2
s = s-(2*a/3)
print("%.2f"%(s))
    
