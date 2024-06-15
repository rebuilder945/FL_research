def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
     a=1
     b=1
     c=1
     while a<num:
            b*=a
            c+=1/b
            a+=1
     print("%.6f"%c)
main()


