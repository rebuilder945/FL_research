a=str(input())
b=str(input())
t=a+b
if "red"in t and"blue"in t:
    print("purple")
elif "red"in t and"yellow"in t:
    print("orange")
elif "blue"in t and"yellow"in t:
    print("green")
else:
    print("error")
