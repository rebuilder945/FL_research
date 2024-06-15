height = eval(input())
N = eval(input())
height1 = height
for x in range(N-1):
    height1/=2
    height+=(height1)*2

print('{:.2f}'.format(height))

