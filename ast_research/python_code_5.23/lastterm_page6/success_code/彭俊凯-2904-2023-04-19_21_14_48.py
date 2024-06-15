def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=[]
    for i in range(1,a+1):
        s.append((a/9)*(10**i-1))
    print("%.d"%(sum(s)))
main()

