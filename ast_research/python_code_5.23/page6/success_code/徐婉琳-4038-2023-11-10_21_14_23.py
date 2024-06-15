c=input()
zm,kg,sz,qt=0,0,0,0
for x in c:
    if "a"<=x<="z" or "A" <=x<="Z":
        zm+=1#判断字母是否在字母表中
    elif x==" ":
        kg+=1#判断输入的是否为空格
    elif "0"<=x<="9":
        sz+=1
    else:
        qt+=1
print(zm,kg,sz,qt)        
