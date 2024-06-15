def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e,b=1,1
    for i in range(1,num+1):
        a=1/i
        b=b*a
        e=e+b
    print("%.6f"%(e))
main()


