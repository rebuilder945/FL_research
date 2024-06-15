def main():
    num = eval(input())
    calculate_e(num)
def j(n):
    a=1
    if n==0:
        a=1
    else:
        for i in range(1,n+1):
           a=a*i
    return a
def calculate_e(num):
    c=0
    for n in range(num+1):
        c+=1/(j(n))
    print("%.6f"%(c))
main()


