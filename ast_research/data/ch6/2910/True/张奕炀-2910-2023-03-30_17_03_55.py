length = eval(input())
N = eval(input())
length0 = 0
lengthcopy = length
for i in range(N-1):
    length0 = length0 + lengthcopy * pow(0.5,i)
length0 = length0 + length
print("%.2f"%(length0))
