def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    t=1
    l=0
    for i in range(num):
        t=t*(l+1)
        s=s+1/t
        l=l+1
    print("%.6f"%s)    
main()


