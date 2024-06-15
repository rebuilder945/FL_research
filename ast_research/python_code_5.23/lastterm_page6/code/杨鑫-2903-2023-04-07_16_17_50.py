def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    fm = 1
    for i in range(1,num+1):
        fm = fm*i
        e = e + 1/fm
return e
print("%.6f"%e)
main()


