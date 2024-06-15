def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    e=1
    s=1
    for i in range(1,1+a):
        e+=1/(s*i)
    print("%.6f"%e)
main()


