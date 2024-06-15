def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(1,num+1):
        chengji=1
        for j in range(1,i+1):
            chengji=chengji*j
        e+=1/chengji
    print("%.6f"%e)
main()


