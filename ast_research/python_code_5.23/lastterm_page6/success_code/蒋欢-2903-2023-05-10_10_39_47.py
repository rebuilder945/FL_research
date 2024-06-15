def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    for x in range(1,num+1):
        e+=1/x
    print("%.6f"%e)
main()


