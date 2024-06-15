def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    for i in range(num):
        A = i + 1
        x = 1
        for a in range(A):
            x = (1/(a+1))*x
        e = e + x 
    print("%.6f"%(e))
main()


