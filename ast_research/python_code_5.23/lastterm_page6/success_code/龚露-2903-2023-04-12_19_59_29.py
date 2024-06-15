def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    i = 1
    a = 1
    e = 1
    while i < num + 1:
        a = a*i
        e = e+1/a
        i = i +1
    print("%.6f" % e)
        
        
main()


