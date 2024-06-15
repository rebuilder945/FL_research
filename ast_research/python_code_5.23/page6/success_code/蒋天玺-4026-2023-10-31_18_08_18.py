n = eval(input())
#n+1/n
sum = 0
for x in range(1,n+1):
    sum+=(x+1)/x
print("%.2f"%sum)
