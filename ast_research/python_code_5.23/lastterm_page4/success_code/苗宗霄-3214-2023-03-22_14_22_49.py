arr = [1,0,2,0,2,0,0]
for i in range(len(arr)):
    if arr[i]== 0:
        for j in range(i,len(arr)-1):
            if arr[j+1]!=0:
                arr[i],arr[j+1]=arr[j+1],arr[i]
                break

print(arr)
