# 定义原色和次生色的对应关系
color_map = {
    ('red', 'blue'): 'purple',
    ('red', 'yellow'): 'orange',
    ('blue', 'yellow'): 'green'
}

# 获取用户输入的两种原色
color1 = input()
color2 = input()

# 判断输入是否合法
if color1 not in ['red', 'blue', 'yellow'] or color2 not in ['red', 'blue', 'yellow']:
    print('error')
elif color1 == color2:
    print('error')
else:
    # 查找对应的次生色并输出
    secondary_color = color_map.get((color1, color2)) or color_map.get((color2, color1))
    if secondary_color:
        print(secondary_color)
    else:
        print('error')

