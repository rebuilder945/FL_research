a=input()
b=input()
y=["red","blue","yellow"]
if (a  not in y) or (b not in y) or (a==b):
    print("error")
elif b==y[0] and a==y[1] or(b==y[1] and a==y[0]):
    print("pueple")
elif b==y[0] and a==y[2] or(b==y[2] and a==y[0]):
    print("orange")
else:
    print("green")
    
