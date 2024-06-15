def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    d=0
    c=a
    for j in range(1,c+1):
        m=0
        while True: # 计算第j个需要累加的数值
            if j >0:
                e = a * 10 ** (j - 1)
                m=m+e
                j=j-1
            else:
                break
        d=d+m # 将所有所有需要的值累加得到结果


    print(d)
main()

