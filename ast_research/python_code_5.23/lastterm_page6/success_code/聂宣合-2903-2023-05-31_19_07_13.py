def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    mid=1
    sums=0
    for i in range(1,num+1):
        mid=mid*(1/i)
        sums+=mid
    print("%.6f"%(sums+1))
main()


