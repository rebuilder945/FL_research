a=input()
dict={}
while a !="q":
    if a not in dict:
        dict[a]=1
    else:
        dict[a]+=1
    a=input()
max_value=max(list(dict.values()))
for key,value in dict.items():
    if value==max_value:
        print(key,value)
