lst1=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36,]
a=int(input())
if a in lst1:
    print("red")
elif a==0:
    print("green")
elif a>36 or a<0:
    print("error")
else:
    print("black")
