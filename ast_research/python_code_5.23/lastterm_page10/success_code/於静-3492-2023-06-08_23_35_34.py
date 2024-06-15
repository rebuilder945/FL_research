shuju=input() or "None"
if shuju == "None":
    print(shuju)
else:
    for x in shuju:
        if shuju.count(x)==1:
            print(x)
            break
    
