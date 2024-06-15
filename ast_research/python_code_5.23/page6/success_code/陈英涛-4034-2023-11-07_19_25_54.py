a = {"red","blue","yellow"}
c1 = input()
c2 = input()
s = {c1,c2}
if c1 != c2 and c1 in a and c2 in a:
    if s == {"blue",'red'}:
        print("purple")
    if s == {"red","yellow"}:
        print("orange")
    if s == {"yellow","blue"}:
        print("green")
else:
    print("error") 
