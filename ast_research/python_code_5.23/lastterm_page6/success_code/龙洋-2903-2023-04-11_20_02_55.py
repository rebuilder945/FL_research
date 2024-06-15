def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    q=1
    e=1
    for x in range(n):
        q=q*(x+1)
        e=e+1/q
    print("%.6f"%(e))
main()


