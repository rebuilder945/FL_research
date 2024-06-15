def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(N):
    dList = [i for i in range(1,N+1)]
    tList = []
    p = 1
    for j in dList:
        for k in range(1,j+1):
            p = p * k
    tList.append(1/p)
    result = sum(tList)
    print('%.6f'%result)
main()


