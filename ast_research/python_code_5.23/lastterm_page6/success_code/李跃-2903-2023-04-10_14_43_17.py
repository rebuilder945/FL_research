def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    i=0
    a=1
    for n in range(1,num+1):
        while i<n:
            i=i+1
            a=a*i
        e=e+1/(a)
    print("%.6f"%(e))
main()


