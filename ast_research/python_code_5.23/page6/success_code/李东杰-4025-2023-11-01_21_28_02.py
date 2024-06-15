def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    a=1
    for x in range(num):
        a=a*(x+1)
        e=e+1/a
    print("%.6f"%(e))
        
        
main()


