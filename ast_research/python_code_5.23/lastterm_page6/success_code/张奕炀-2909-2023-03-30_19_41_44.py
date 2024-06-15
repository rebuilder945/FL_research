number = eval(input())
def chazhao(number):
    list0 = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
    ['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
    ['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
    ['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
    ['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
    start = 0
    end = len(list0) - 1
    while start < end:
        mid = (start + end) // 2
        if int(list0[mid][0]) == number:
            return("".join(list0[mid]))
        elif int(list0[mid][0]) > number:
            end = mid - 1
        else:
            int(list0[mid][0]) < number
            start = mid + 1
    return 'None'
print(chazhao(number))
