def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
       jishu=1
       for i in range(1,x+1):
            for j in range(1,i+1):
            jishu+=1/j
       print('%.6f'%jishu)
main()


