def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for x in range(1,num+1):
        p=1
        for y in range(1,x+1):
            p*=y
        e+=1/p
    print("%.6f"%e)
main()


