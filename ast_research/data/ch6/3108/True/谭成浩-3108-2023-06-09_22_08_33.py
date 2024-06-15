def count(str):
    mydict = {}
    for i in str:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    return mydict


mylist = eval(input())
result = count(''.join(mylist))
key_value = sorted(result.keys())
dict_sort = {}
for key in key_value:
    dict_sort[key] = result[key] 
for key in dict_sort:
    print(key + ',' + str(dict_sort[key])) 

