a = input()
b = input()
if {a,b} == {"red","blue"}:
    print("purple")
elif {a,b} == {"red","yellow"}:
    print("orange")
elif {a,b} == {"blue","yellow"}:
    print("green") 
else:
    print("error")
