def find_str(arr):
    dic={}
    for x in arr:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    for x in arr:
        if dic[x]==1:
            return x
        else:
            return None
s=input()
if len(s)==0:
    print("None")
else:
    print(find_str(s))

