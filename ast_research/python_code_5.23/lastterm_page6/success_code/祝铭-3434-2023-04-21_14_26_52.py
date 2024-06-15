c1 = input()
c2 = input()
pcom = ["red","blue"]
ocom = ['red','yellow']
gcom = ['blue','yellow']
if c1 != c2:
    if c1 in pcom and c2 in pcom :
        print("purple")
    elif c1 in ocom and c2 in ocom :
        print("orange")
    elif c1 in gcom and c2 in gcom :
        print("green")
    else:
        print("error")
else:
    print("error")
