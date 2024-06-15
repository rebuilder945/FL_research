def main():
    num = eval(input())
    calculate_e(num)
def calculate_e():
    e=1
    for i in range(num):
        a=1/(i+1)
        e+=a
    print ("%.6f"%(e))

main()


