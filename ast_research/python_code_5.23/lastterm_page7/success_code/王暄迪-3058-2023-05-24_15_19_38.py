keys=input()
dict1={}
while keys!="q":
    dict1[keys]=dict1.get(keys,0)+1
    keys=input()
print(max(dict1.values()))
