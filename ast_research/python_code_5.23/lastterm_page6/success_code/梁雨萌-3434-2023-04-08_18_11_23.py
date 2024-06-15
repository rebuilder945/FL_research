def color(a,b):
    if a and b in ["red","blue"]:
        return("purple")
    if a and b in ["red","yellow"]:
        return("orange")
    if a and b in ["blue","yellow"]:
        return("green")
    
a=input()
b=input()
list=["red","blue","yellow"]
if a == b or a and b not in list:
    print("error")
else:
    word=color(a,b)
    print(word)

