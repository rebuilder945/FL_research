def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for x in range(1,num+1):
        a=1
        for i in range(1,x+1):
            a=a*i
        e=e+1/a
    print("%.6f"%(e))
main()


