def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    e=1
    for i in range(1,num+1):
       a=a/i
       e+=a
    print("%.6f"%e)
main()


