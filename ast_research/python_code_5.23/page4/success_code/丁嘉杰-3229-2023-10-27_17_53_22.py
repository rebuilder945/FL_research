def findJishu(array):
    if array==None:
        return 0
        print("False")
    
    dic=dict()
    length=len(array)
    for i in range(length):
        if array[i] not in dic:
            dic[array[i]]=1
        else:
            dic[array[i]]=0
    for key,value in dic.items():
        if value==1:
            print(key)
if __name__ == '__main__':
    array=eval(input())
    findJishu(array)
