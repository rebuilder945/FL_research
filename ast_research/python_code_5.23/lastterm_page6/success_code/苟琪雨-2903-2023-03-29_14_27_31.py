def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    result1=0
    lst=[]
    for i in range(1,num+1):
        for x in range(1,i+1):
            result1=result1+x
            lst.append(result1)
    result2=0
    for p in range(0,num):
        result2=result2+1/int(lst[p])
    print('%.6f'%result2)
main()


