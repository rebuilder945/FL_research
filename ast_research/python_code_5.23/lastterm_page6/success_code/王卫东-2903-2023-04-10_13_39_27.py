def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    b=1
    for x in range(1,a+1):
        c=1
        for y in range(1,x+1):
            c = c*y
        b = b+1/c 
    print("%.6f"%b)  
main()


