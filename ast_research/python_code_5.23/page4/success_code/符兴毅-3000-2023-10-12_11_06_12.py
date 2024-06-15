lis = eval(input())
i = 0
sum = 0
while i<len(lis):
    sum+=lis[i]
    i+=1
aim = sum/len(lis)
print('%.2f'%aim)
