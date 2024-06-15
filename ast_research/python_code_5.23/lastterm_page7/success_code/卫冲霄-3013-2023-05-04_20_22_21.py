GDP={}
user_input=input()
while user_input !="ok":
    k,v=user_input.split()
    GDP[k]=int(v)
    user_input=input()
ls1=list(GDP.keys())
ls2=list(GDP.values())
print(ls1)
print(ls2)
print("yes" if "India" in ls1 else "no")
print(sum(ls2))
