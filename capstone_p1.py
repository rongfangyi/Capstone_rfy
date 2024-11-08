import turtle

# 设置画布
screen = turtle.Screen() #创建绘图窗口
screen.bgcolor("white") #背景白色
screen.title("Rainbow Flower") #起名

# 初始化画笔
pen = turtle.Turtle() #创建画笔
pen.speed(5) #移动速度为5 （1-10）
pen.width(2) #画笔宽度2

# 定义彩虹颜色
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


# 画花瓣
def draw_petal(color): #绘制一个单独的花瓣
    pen.color(color)
    pen.begin_fill() #填充形状
    pen.circle(60, 60)  # 左侧弧
    pen.left(120)
    pen.circle(60, 60)  # 右侧弧
    pen.left(120)
    pen.end_fill()


# 画彩虹花
def draw_rainbow_flower(): #画完整的花朵
    pen.penup() #移动时画笔不会画出线条（抬笔）
    pen.goto(0, -30)  #调整中心位置
    pen.setheading(0)  #方向向上
    pen.pendown() #放笔

    for i in range(7):  # 绘制七个彩虹色花瓣
        draw_petal(rainbow_colors[i % len(rainbow_colors)])
        pen.right(360 / 7)  # 每次旋转一定角度


# 主函数
draw_rainbow_flower()

#隐藏光标
pen.hideturtle()

# 完成绘制
turtle.exitonclick()  # 当点击时退出
