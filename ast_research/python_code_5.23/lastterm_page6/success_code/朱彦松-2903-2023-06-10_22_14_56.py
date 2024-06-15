def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    s=[]
    for x in range(1,num+1):
        a=a*x
        b=1/a
        s.append(b)
    c=sum(s)+1
    print("%.6f"%(c))
main()


