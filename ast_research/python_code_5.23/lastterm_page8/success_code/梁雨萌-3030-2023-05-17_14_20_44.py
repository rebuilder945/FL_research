lis1 = list(input().split(','))
Lis2 = input().split(',')
lis2 = [int(x) for x in Lis2]
lis = []



for i in range(0,len(lis1)):
    lis.append([lis1[i],lis2[i]])

for i in range(0,len(lis)-1):
    min = i
    for j in range(i+1,len(lis)):
        if lis[min][1] > lis[j][1]:
            min = j
    lis[i],lis[min] = lis[min],lis[i]
    
    

print(lis)
