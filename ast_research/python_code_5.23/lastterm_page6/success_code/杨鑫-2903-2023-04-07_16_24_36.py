def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a = 1
    fm = 1
    for i in range(1,num+1):
        fm = fm*i
        a = a + 1/fm
    print("%.6f"%a)
main()


