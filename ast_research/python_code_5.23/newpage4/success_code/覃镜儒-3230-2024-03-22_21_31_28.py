i=eval((input()))
i.sort(reverse=True)
if all(element==0 for element in i):
    print("0")
else:
    for element in i:
        print(element,end="")
