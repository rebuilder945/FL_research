def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(num):
        s=1
        for x in range(x+1):
            s*=(x+1)
        e+=1/s
    print ("%.6f"%e)

main()


