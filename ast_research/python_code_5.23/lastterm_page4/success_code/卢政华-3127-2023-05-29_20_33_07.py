n = int(input()) 
x = [i+1 for i in range(n)]

x[n-1] = x[n]
print(x)
