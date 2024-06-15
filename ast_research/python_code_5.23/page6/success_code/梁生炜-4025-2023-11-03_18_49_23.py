def main():
    num = eval(input())
    calculate_e(num)
def  main():
        num  =  eval(input())
        calculate_e(num)
def calculate_e(num):
        e=1
        lst=range(num+1)
        for i in range(num):
                if i==0:
                        m=1
                else:
                        m=len((num)*((num[1]+num[i+1])))/2
                e+=1/m
        print("%.6f"%e)
main()
      
main()


