a=input()
b=input()
ls=['red','blue','yellow']
if a==b or a not in ls or b not in ls:
    print("error")
elif a== "red" and b== "blue" or b== "red" and a== "blue":
    print("purple")
elif a== "red" and b== "yellow" or b== "red" and a== "yellow":
    print("orange")
elif a== "blue" and b== "yellow" or b== "blue" and a== "yellow":
    print("green")

