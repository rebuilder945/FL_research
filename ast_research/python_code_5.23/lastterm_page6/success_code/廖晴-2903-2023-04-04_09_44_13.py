def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    su=1
    for i in range(1,num+1):
        s*=i
        su+=1/s
    print("%.6f"%su)
main()


