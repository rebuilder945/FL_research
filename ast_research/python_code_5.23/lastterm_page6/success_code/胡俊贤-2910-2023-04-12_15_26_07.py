h=input()
N=int(input())
fantan=0
a=h
for i in range(N-1):
    h=h*0.5
    fantan+=2*h
yigong=a+fantan
print('%.2f'%yigong)
