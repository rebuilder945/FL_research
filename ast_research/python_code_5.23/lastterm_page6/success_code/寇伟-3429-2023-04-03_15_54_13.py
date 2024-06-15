a=input()
english_count=0
space_count=a.count(' ')
num_count=0
fuhao_count=0
for i in a:

    if i in list(range(65,122)):
        english_count+=1
    elif i in list(range(49,57)):
        num_count+=1
    elif i in list(range(33,42)):
        fuhao_count+=1
print(english_count,space_count,num_count,fuhao_count)

