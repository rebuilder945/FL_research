color1=input()
color2=input()
lis1=['red','blue','yellow']
lis2=['purple','orange','green']
if color1 not in lis1 or color2 not in lis1:
    print('error')
else:
    if color1==color2:
        print('error')
if color1==lis1[0] and color2==lis1[1]:
    print(lis2[0])
if color1==lis1[0] and color2==lis1[2]:
    print(lis2[1])
if color1==lis1[1] and color2==lis1[0]:
    print(lis2[0])
if color1==lis1[1] and color2==lis1[2]:
    print(lis2[2])
if color1==lis1[2] and color2==lis1[0]:
    print(lis2[1])
if color1==lis1[2] and color2==lis1[1]:
    print(lis2[2])
