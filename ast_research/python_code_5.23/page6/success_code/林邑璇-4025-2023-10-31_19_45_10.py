def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(1,1+num):
        a=1
        for x in range(1,i+1):
            a=a*1/x
        e+=a
    print("%.6f"%(e))
main()


