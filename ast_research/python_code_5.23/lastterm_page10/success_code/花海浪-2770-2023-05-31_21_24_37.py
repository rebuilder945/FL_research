a=input()
b=input()
for x in a:
    for y in b:
        if x not in b or y not in a:
            print("False")

else:
    print("True")
