def find(arr):
    dic={}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]]+=1
        else:
            dic[arr[i]]=1
    for i in range(len(arr)):
        if dic[arr[i]]==1:
            return arr[i]
if __name__=='main__':
    arr=input("")
    print(find(arr))
