color_all=("red","blue","yellow")
n=input()
m=input()
color_all=set(color_all)
shuru=(n,m)
shuru=set(shuru)
if n==m or shuru&color_all==[]:
    print("error")
elif shuru==("red","blue"):
    print("purple")
elif shuru==("red"and "yellow"):
    print("orange")
elif shuru==("blue","yellow"):
    print("green")
else:
    pass
