__name__=input()
name1=0
name2=0
name3=0
name4=0
list=[__name__[0::]]
for i in range(len(list)):
    if "0"<=list[i]<="9":
        name1+=1
    elif "a"<=list[i]<="z":
        name2+=1
    elif list[i]==" ":
        name3+=1
    else:
        name4+=1    
print(" ".join[name1,name2,name3,name4])
