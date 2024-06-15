
def getKey(dic,value):
    if value not in dic.values():
        return None
    result=set()
    for key in dic:
        if dic[key] == value:
            result.add(key)
    return result
a =eval(input())
dict = {}
for key in a:
    dict[key] = dict.get(key, 0) + 1
getKey(dict,1)
