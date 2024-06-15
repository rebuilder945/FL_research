h = eval(input())
N = eval(input())
hList = [h]
for i in range(1,N+1):
    hList.append((0.5) ** i * h * 2)
nHei = sum(hList)
print('%.2f'%nHei)
