sName = input("请输入飞机名称:")
a = float(input("请输入加速度:"))
v = float(input("请输入速度:"))
sText = "The acceleration of %s is %.2f M/s, the take-off speed is %.2f M/s, and the shortest take-off runway length is "\
"%.2f M." % (sName, a, v, v*v/(2*a))
print(sText)
