def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
    x=0
    y=0
    m=0
    while 1==1:
        x+=1
        y+=x
        s=1/y
        m+=s
        if x >=n:
            print(y)
            print("%.6f"%(m+1))
            break
main()


