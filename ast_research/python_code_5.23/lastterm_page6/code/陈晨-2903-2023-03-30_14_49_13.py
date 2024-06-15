def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    k=num
    s=1
    for x in range(k):
        p=1
        for k in range(1,x+1):
        p*=k
        s+=1/p
    print("%.6f"%(s))
main()


