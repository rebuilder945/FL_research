list=eval(input())
re=[]
for i in list:
    if i not in re:
        re.append(i)
    else:
        re.remove(i)
        
print(re)
