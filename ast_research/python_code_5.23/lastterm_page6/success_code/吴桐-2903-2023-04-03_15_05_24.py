def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    e=1
    for i in range(num):
        m=1
        for x in range(i+1):
            m*=x+1
        e+=1/m
    print("%.6f"%(e))
main()


