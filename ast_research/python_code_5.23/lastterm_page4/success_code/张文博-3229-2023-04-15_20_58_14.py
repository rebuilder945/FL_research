m=eval(input())
dict={}
for key in m:
    dict[key]=dict.get(key,0)+1
n=dict.get(key,1)
print(n)
