def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
        e=1
        for x in range(1,n+1):
                a=1
                for y in range(1,x+1):
                        a*=y
                e+=1/a
        print("%.6f"%(e))
main()


