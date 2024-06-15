def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        i=0
        e=[1]
        while num>i:
                x=1/(i+1)
                e.append(x)
                i=i+1
        y=sum(e)
        print("%.6f"%(y))
main()


