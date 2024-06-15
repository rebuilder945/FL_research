n=input().lower()
color=["red","bule","yellow"]
m=input().lower()
if n!=m and n in color and m in color:
    if n in color[0:2] and m in color[0:2]:
        print("purple")
    elif n in color [1:3] and m in color [1:3]:
        print("green")
    else:
        print("orange")
else:
    print("error")        


