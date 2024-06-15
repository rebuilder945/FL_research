def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    e=0
    b=1
    c=1
    while a<=num:
        e+=b
        b=b/a
        a=a*c
        c+=1
    print("%.6f"%(e))
main()


