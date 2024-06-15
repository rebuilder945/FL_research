s=input()
dic={}
a=0
for i in s:
    if "a"<=i<="z":
        dic["xiao"]=dic.get("xiao",0)+1
    elif "A"<=i<="Z":
        dic["da"]=dic.get("da",0)+1
    elif i in "~!@#$%^&*()_=-/,.?<>;:[]{\}|":
        dic["te"]=dic.get("te",0)+1
    elif i.isdigit():
        dic["shu"]=dic.get("shu",0)+1
if len(s)>=8:
    a+=1
for i in dic.values():
    if i !=0:
        a+=1
print(a)

    
