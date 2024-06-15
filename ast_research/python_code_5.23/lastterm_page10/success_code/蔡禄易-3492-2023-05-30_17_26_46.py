a = input()
b = [x for x in a.replace(" ","")]
c = []
if b != []:
    for i in b:
        if i not in c:
            c.append(i)
    print(c[0])
else:
    print("None")
    
