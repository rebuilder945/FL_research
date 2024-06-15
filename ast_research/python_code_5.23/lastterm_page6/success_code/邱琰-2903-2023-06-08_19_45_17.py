def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    c=1
    for i in range(1,num+1):
        c=c/i
        e+=c
    print("%.6f"%(e))
main()


