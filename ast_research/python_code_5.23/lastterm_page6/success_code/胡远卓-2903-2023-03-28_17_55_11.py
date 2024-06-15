def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    res,p=1.0,1.0
    for x in range(num):
        p/=(x+1)
        res+=p
    print("%.6f"%(res))
main()


