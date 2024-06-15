def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        x = 1
        e = 1
        r = 1
        for i in range(1,num+1):
                while r <= i:
                        x = x * r
                        r = r + 1
                e = e + 1/x
        print("%.6f"%e)           
main()


