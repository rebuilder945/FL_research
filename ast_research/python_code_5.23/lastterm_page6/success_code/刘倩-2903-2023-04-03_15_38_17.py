def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    fenmu = 1
    for i in range(1,num+1):
        fenmu*=i
        e+=1/(fenmu)
    print(e)
main()


