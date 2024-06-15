col1=input()
col2=input()
final=set([col1,col2])
if final=={"red","blue"}:
    print("purple")
elif final=={"red","yellow"}:
    print("orange")
elif final=={"blue","yellow"}:
    print("green")   
else:
    print("error")
