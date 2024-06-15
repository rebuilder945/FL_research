names=input().split(",")
grades=list(eval(input()))
bond=[]
for x in list(range(len(names))):   
    ml=[names[x],grades[x]]    
    bond.append(ml)
bond.sort(key=lambda x:x[1])
print(bond)
