def main():
    num = eval(input())
    calculate_e(num)

       
def calculate_e(num):
        d =[]
        b =1
        
        for i in range(1,num+1):
                b = b*i
                a = 1/b
                d.append(a)
        m =sum(d)+1
        print("%.6f"%m)
main()


