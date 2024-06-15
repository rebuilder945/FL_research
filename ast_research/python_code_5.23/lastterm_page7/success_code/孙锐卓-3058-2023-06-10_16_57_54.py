str1 = input()
strs={}
while str1 != 'q':
    strs[str1] = strs.get(str1,0) + 1
    str1 = input()
max_count=0
for key in strs:
    if strs[key]>max_count:
        max_count=strs[key]
        max_key = key
print(max_key,max_count)

