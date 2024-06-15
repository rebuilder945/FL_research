data=[
    ['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']
]

for i in data:
    i[0]=int(i[0])

number=int(input())

begin=0
end=len(data)-1

def printResult(x):
    print(data[x][0],data[x][1],sep="")

while end > begin + 1:
    mid=(begin+end)//2
    if data[begin][0]==number:
        printResult(begin)
        break
    elif data[end][0]==number:
        printResult(end)
        break
    else:
        if data[mid][0]==number:
            printResult(mid)
            break
        elif data[mid][0]<number:
            begin=mid
        else:
            end=mid
else:
    print("None")
