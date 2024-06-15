a = list(input().split(" "))
b = list(input().split(" "))  
n = int(b[0])
m = int(b[1]) 
a[n],a[m] = a[m],a[n]
print(a)
