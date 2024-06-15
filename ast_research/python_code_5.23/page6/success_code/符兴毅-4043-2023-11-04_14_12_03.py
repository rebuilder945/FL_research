aim = ''.join(eval(input()))
aim_lis = []
# print(aim)
for i in range(int(ord('a')),int(ord('z'))+1):
    if chr(i) in aim:
        num = aim.count(chr(i))
        zuhe = chr(i)+','+str(num)
        aim_lis.append(zuhe)
for i in aim_lis:
    print(i)

