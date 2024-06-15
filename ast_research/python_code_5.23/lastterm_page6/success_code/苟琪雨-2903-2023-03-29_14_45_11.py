def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    for i in range(1,num+1):
        result1=0
        for x in range(1,i+1):
            result1=result1+x
        lst.append(result1)
    result2=0
    for p in range(0,num):
        result2=result2+1/int(lst[p])
    result3=result2+1
    print('%.6f'%result3)
main()


