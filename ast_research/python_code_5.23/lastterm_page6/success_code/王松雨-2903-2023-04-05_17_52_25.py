def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    e=0
    for i in range(1,num+1):
        e+=a
        a=a/i
    print("%.6f"%e)
main()


