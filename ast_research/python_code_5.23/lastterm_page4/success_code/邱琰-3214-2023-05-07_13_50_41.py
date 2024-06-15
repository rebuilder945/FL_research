lst=eval(input())
lst.sort(reverse=True)
key=""
for i in range(len(lst)):
    key+=str(lst[i])
print(int(key))
