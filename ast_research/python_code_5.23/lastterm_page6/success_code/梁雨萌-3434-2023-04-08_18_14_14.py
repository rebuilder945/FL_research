def color(a,b):
    if a and b in ["red","blue"]:
        return("purple")
    elif a and b in ["blue","yellow"]:
        return("green")
    elif a and b in ["red","yellow"]:
        return("orange")

    
a=input()
b=input()
list=["red","blue","yellow"]
if a == b or a not in list or b not in list:
    print("error")
else:
    word=color(a,b)
    print(word)

