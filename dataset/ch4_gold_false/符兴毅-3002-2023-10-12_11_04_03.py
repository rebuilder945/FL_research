lis = eval(input())
print(len(lis))
i = 0
sum = 0
while i<len(lis):
    sum+=lis[i]
    i+=1
aim = sum/len(lis)
if aim%int(aim)==0:
    print(int(aim))
else:
    print('%.2f'%aim)
