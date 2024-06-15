def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        kong = [1]
        kong2 = []
        y = 1
        for i in range(1,num+1):
                y = y*i
                kong.append(y)
        for i in kong:
                x = 1/i
                kong2.append(x)
        print("%.6f"%(sum(kong2)))   
main()


