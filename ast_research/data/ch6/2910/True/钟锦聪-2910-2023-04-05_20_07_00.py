height = eval(input())
n = int(input())
s = height
for x in range(n-1):
    height = height/2
    s += height*2
print("%.2f"%s)
