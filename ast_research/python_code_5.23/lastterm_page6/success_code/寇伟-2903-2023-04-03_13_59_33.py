def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    s=1
    for i in range(0,num+1):
        if i == 0:
            e+=1
        else:
            for j in range(1,i+1):
                s*=(1/i)
            e+=s
    print("%.6f"%e)
main()


