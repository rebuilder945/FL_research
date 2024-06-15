lis = list(input())
ten = ['X', 'x', 'Ⅹ']
ID = ["10" if x in ten else x for x in lis]     #将罗马数字Ⅹ和字母X替换为10
W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
sum = 0
for i in range(17):     #https://blog.zeruns.tech
    sum = sum + int(ID[i]) * W[i]
if Checkcode[sum % 11] == int(ID[17]):
    print('Correct')
else:
    print('Wrong')

