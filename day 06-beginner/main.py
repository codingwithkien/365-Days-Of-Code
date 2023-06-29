# import turtle
# tp = turtle.Turtle()
# tp.fd(100)
# tp.rt(90)
# tp.fd(100)
# tp.rt(90)
# tp.fd(100)
# tp.rt(90)
# tp.fd(100)

# import turtle
# tp = turtle.Turtle()
# tp.fd(300)
# tp.rt(90)
# tp.fd(150)
# tp.rt(90)
# tp.fd(300)
# tp.rt(90)
# tp.fd(150)
# tp.rt(90)

# import turtle
# tp = turtle.Turtle()
# tp.circle(50) # 50 là bán kính hình tròn


# import turtle
# tp = turtle.Turtle()
# tp.fd(100)
# tp.lt(120)
# tp.fd(100)
# tp.lt(120)
# tp.fd(100)
import turtle
# tp = turtle.Turtle()
# tp.pencolor("#4FFF08")
# tp.fillcolor("#FFD208")
# tp.pensize(8)
# tp.speed(1)
# tp.begin_fill()
# tp.circle(110)
# turtle.bgcolor("blue") # bgcolor
# tp.end_fill()

# turtle.goto(0, 100)
# turtle.goto(-100, 0)
# turtle.goto(0, 0)





# Viết chương trình vẽ và tô màu cho hình vuông
# với kích thước, màu nhập từ bàn phím (màu có dạng #RRGGBB)

































# import turtle
# t = turtle.Pen()
# turtle.bgcolor("black")
# colors = ["red", "yellow", "blue", "green"]
# for x in range(200):
#     t.pencolor(colors[x%4])
#     t.forward(x)
#     t.left(91)



# len(): độ dài list
# min(): giá trị nhỏ nhất
# max(): tìm giá trị lowns nhất
# sort(reverse =  False): sắp xếp tăng dần
# sort(reverse =  True): sắp xếp giảm dần

# a = [1, 4, 2, 6, 5, 8, 0]
# print("Độ dài của list là", len(a))
# print("Giá trị nhỏ nhất:", min(a))
# print(max(a))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# Taọ một list có n phần tử (n nhập từ bàn phím) sau đó thêm các phần tử nhập được vào list,
# thêm số 10 vào list,
# in list ra man hinh
# tìm min, max, sum, len
# kiểm tra 10 có trong list hay không
# cắt 2 phần tử cuoois
# cắt 3 phần tử đầu tiên
# sắp xếp tăng dần và giảm dần
#
# import turtle
# turtle.showturtle()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)










import turtle as t
import time as ti

def rectangle(hor,ver,col):
    t.pendown() #tạo con trỏ
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')
#Vẽ bàn chân

t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#Vẽ chân

t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#Vẽ thân

t.goto(-90,100)
rectangle(100,150,'red')

#Vẽ tay

t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-150,110)
rectangle(15,40,'grey')
t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')

#Vẽ cổ

t.goto(-50,120)
rectangle(15,20,'grey')

#Vẽ đầu

t.goto(-85,170)
rectangle(80,50,'red')
t.goto(-60,160)

#Vẽ mắt miệng:
rectangle(30,10,'white')
t.goto(-60,160)
rectangle(5,5,'black')
t.goto(-45,155)
rectangle(5,5,'black')
t.goto(-65,135)
t.right(5)
rectangle(40,5,'black')

#Vẽ bàn tay:

t.goto(-155,130)
rectangle(25,25,'green')
t.goto(-147,130)
rectangle(10,15,t.bgcolor())
t.goto(50,130)
rectangle(25,25,'green')
t.goto(58,130)
rectangle(10,15,t.bgcolor())

t.hideturtle()
ti.sleep(10)
t.hideturtle()


# import turtle as t
# import time
# t.hideturtle()
# t.write("Hello World")
# t.style("courier", 20)
# time.

# def tong(a, b):
#     tong_a_b = a + b
#     return tong_a_b
#
# print(tong(4, 1))



# import turtle as t
# def rectangle(dai, rong, mau):
#     t.pendown()
#     t.pensize(1)
#     t.color(mau)
#     t.begin_fill()
#     for i in range(2):
#         t.forward(dai)
#         t.left(90)
#         t.forward(rong)
#         t.left(90)
#     t.end_fill()
#     t.penup()
#
# rectangle(100, 90, "red")













