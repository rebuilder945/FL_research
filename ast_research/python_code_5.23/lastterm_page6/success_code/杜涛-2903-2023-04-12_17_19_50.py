def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    b=[]
    for i in range(1,num+1):
        a=a*i
        c=1/a
        b.append(c)   
    # print(b)    
    print("%.6f"%(sum(b)+1))
main()


