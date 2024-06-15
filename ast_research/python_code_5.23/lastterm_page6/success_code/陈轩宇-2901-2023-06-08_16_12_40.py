list1=[]
a=0
while a!="#":
    a = input()
    if a!="#":
        b=eval(a)
        list1.append(b)
        
jishu = len(list1)
sum1 = sum(list1)
print(jishu,sum1)

    
