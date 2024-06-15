A = print()
B = print()
hun = {A,B}
T = {'red','blue','yellow'}
P = {'red','blue'}
G = {'blue','yellow'}
O = {'red','yellow'}
if A not in T or B not in T or A == B:
    print('error')
elif hun == P:
    print("purple")
elif hun == G:
    print("green")
elif hun == O:
    print("orange")

