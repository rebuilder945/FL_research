A = print()
B = print()
P = {'red','blue'}
G = {'blue','yellow'}
O = {'red','yellow'}
if A in P and B in P:
    print("purple")
elif A in G and B in G:
    print("green")
elif A in O and B in O:
    print("orange")
else:
    print("error")
