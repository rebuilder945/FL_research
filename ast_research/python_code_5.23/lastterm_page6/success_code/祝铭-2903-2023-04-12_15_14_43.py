def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 1
    for i in range(num):
        if i == 0:
            m+=1
        else:
            m = m+1/(i*i+i)
    print("%.6f"%(m))
main()


