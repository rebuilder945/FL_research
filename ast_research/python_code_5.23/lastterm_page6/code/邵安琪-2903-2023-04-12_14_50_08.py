def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    while num>=1:
        e+=1/num!
        num-=1
    print("%.6f"%(e))
main()


