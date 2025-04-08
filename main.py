import tkinter as tk
import math
import time

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("时钟")

        # 创建指针式时钟画布
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        # 创建数字时钟标签
        self.digital_label = tk.Label(root, font=('Arial', 40), bg='white')
        self.digital_label.pack()

        # 时钟参数
        self.center_x = 200
        self.center_y = 200
        self.radius = 180  # 表盘半径

        # 初始化表盘
        self.draw_clock_face()

        # 创建时钟指针
        self.hour_hand = self.canvas.create_line(0, 0, 0, 0, width=6, fill='black')
        self.minute_hand = self.canvas.create_line(0, 0, 0, 0, width=4, fill='blue')
        self.second_hand = self.canvas.create_line(0, 0, 0, 0, width=2, fill='red')

        # 开始更新时间
        self.update_clock()

    def draw_clock_face(self):
        """绘制表盘和刻度"""
        # 绘制外圆
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            width=4
        )

        # 绘制小时刻度和数字
        for i in range(12):
            angle = math.radians(i * 30 - 90)  # 转换为数学角度
            # 刻度线
            inner = self.radius - 20
            outer = self.radius - 5 if i % 3 == 0 else self.radius - 10
            self.canvas.create_line(
                self.center_x + inner * math.cos(angle),
                self.center_y + inner * math.sin(angle),
                self.center_x + outer * math.cos(angle),
                self.center_y + outer * math.sin(angle),
                width=4 if i % 3 == 0 else 2
            )
            # 数字
            num = 12 if i == 0 else i
            x = self.center_x + (self.radius - 35) * math.cos(angle)
            y = self.center_y + (self.radius - 35) * math.sin(angle)
            anchor = 'center'
            if i == 0:
                anchor = 's'
            elif i == 3:
                anchor = 'e'
            elif i == 6:
                anchor = 'n'
            elif i == 9:
                anchor = 'w'
            self.canvas.create_text(x, y, text=str(num), font=('Arial', 16, 'bold'), anchor=anchor)

    def update_clock(self):
        """更新时钟显示"""
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # 更新数字时钟
        self.digital_label.config(text=time.strftime("%H:%M:%S"))

        # 计算指针角度
        hour_angle = math.radians((hours * 30) + (minutes * 0.5) - 90)
        minute_angle = math.radians((minutes * 6) + (seconds * 0.1) - 90)
        second_angle = math.radians((seconds * 6) - 90)

        # 更新指针位置
        self.update_hand(self.hour_hand, hour_angle, length=self.radius * 0.5)
        self.update_hand(self.minute_hand, minute_angle, length=self.radius * 0.7)
        self.update_hand(self.second_hand, second_angle, length=self.radius * 0.8)

        # 每秒更新一次
        self.root.after(1000, self.update_clock)

    def update_hand(self, hand, angle, length):
        """更新指针位置"""
        x = self.center_x + length * math.cos(angle)
        y = self.center_y + length * math.sin(angle)
        self.canvas.coords(hand, self.center_x, self.center_y, x, y)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()