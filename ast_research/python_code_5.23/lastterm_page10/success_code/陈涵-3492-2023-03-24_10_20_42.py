n=input()or""
if n=="":
    print("None")
else:
    for i in range(len(n)):
        if n.count(n[i])==1:
            print(n[i])
            break



