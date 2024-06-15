def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e,t = 1,1
    for i in range(1,num+1):
            t = t/i
            e += t
    print("%.6f"%e)
main()


