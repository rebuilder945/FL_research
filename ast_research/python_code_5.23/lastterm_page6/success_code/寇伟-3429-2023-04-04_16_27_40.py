a=input()
english_count=0
space_count=0
num_count=0
fuhao_count=0
for i in a:

    if ord(i) in list(range(65,90)) or ord(i) in list(range(97,122)):
        english_count+=1
    elif ord(i) in list(range(30,39)):
        num_count+=1
    elif ord(i) in list(range(33,47)) or ord(i) in list(range(58,64)):
        fuhao_count+=1
    elif ord(i)==32:
        space_count+=1
print(english_count,space_count,num_count,fuhao_count)




