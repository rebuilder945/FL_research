def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=0
    m=num
    e=1
    h=1
    while n<num:
        for i in range(1,m+1):
         h*=i
         e=1/h+e
         n+=1
         m-=1
    print("%.6f"%e)
main()
main()


