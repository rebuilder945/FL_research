from binascii import a2b_base64


A1,A2 = eval(input())
B1,B2 = eval(input())
L = ((A1-B1)**2+(A2-B2)**2)**(1/2)
print("%.2f"%L)
