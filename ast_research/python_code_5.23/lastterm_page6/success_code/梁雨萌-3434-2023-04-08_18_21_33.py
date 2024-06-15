def color(a,b):
    if [a,b]==["red","blue"]or [a,b]==["blue","red"]:
        return("purple")
    elif [a,b]==["blue","yellow"]or [a,b]==["yellow","blue"]:
        return("green")
    elif [a,b]==["red","yellow"]or [a,b]==["yellow","red"]:
        return("orange")

    
a=input()
b=input()
list=["red","blue","yellow"]
if a == b or a not in list or b not in list:
    print("error")
else:
    word=color(a,b)
    print(word)

