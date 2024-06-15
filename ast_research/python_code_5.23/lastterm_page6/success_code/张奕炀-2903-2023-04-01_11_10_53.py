def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    list0 = []
    a = 1
    sum0 = 1
    for i in range(1,num + 1):
        a = a * i 
        sum0 = sum0 + 1 / a
    print("%.6f"%(sum0))
main()


