a = input()
if a == '':
    print("None")
else:
    for x in a:
        if a.count(x)==1:
            print(x)
            break
    

