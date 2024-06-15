color_all={"red","blue","yellow"}
n=input()
m=input()
shuru={n,m}
if n==m or shuru&color_all==[]:
    print("error")
elif shuru=={"red","blue"}:
    print("purple")
elif shuru=={"red","yellow"}:
    print("orange")
elif shuru=={"blue","yellow"}:
    print("green")
else:
    pass
