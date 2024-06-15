lis = list(input())
ten = ['X', 'x', 'Ⅹ']
ID = ["10" if x in ten else x for x in lis]
W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
sum = 0
if len(lis) != 18:
    print("Error")
for i in range(17):
    sum += int(ID[i]) * int(W[i])
if Checkcode[sum % 11-1] == int(ID[17]):
    print('Correct')
else:
    print('Wrong')

