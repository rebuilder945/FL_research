def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    for i in range(1,num+1):
        num*=i
        a=1/(num)
        lst.append(a)
    sum=sum(lst)
    print("%.6f"%sum)
main()


