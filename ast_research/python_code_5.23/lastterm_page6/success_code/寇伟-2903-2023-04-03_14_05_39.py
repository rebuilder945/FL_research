def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    
    for i in range(1,num+1):
        s=1
        for j in range(1,i+1):
            
            s=s*(1/j)
            e+=s
    print("%.6f"%e)
main()


