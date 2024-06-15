def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(1,num+1):
        a=1
        for s in range(1,i+1):
            a*=s
        e+=1/a
    print("%.6f"%(e))
main()


