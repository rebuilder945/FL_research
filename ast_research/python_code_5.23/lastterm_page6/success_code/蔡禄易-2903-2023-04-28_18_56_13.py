def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
     e = 1
     for i in range (1,num):
                num*=i
                e += 1/num
                i += 1
     print("%.6f"%e)
           
main()


