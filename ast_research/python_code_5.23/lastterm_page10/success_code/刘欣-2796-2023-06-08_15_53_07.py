strs=input()
nums=[]
longest=[]
for i in range(len(strs)):
    if '0'<=strs[i]<='9':
        nums.append(strs[i])
        if len(nums)>=len(longest):
            longest=nums.copy()
    else:
        nums=[]
if len(longest)==0:
    print('No digits')
else:
    for i in longest:
        print(i,end='')


