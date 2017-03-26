from tkinter import *
import time
import random
import copy
from tkinter import messagebox

top = Tk()
bg_color = "black"
ground_color = "red"
square = []
colors = ["yellow", "blue", "green", "purple"]
x, y = 10, 20
points = 0

shapes = [[(-1,0), (0,0),  (1,0),  (0,1)  ],  # T
           [ (-1,0), (0,0),  (1,0),   (2,0) ],  # I
           [ (-1,0), (0,0),  (1,0),   (2,0) ],  # double I to make game easier
           [ (1,0), (0,0),  (0,1),   (-1,1) ],  # S
           [ (-1,0), (0,0), (0,1),  (1,1) ],  # Z
           [ (0,0), (0,1),  (1,1),   (1,0)  ],  # O
           [ (-1,1), (0,1), (1,1),  (1,0)  ],  # L
           [ (-1,0), (0,0),  (1,0),  (1,1)  ],  # J
           ]

Canvas = Canvas(top, bg=bg_color, height=y * 20, width=x * 20, bd=0)
for line in range(y):
    for block in range(x):
        square.append(Canvas.create_rectangle(block * 20, line * 20, (block + 1) * 20, (line + 1) * 20, fill=bg_color, outline=bg_color))


class Block():
    def __init__(self, master):
        self.color = random.choice(colors)
        self.shape = random.choice(shapes)
        self.master = master
        self.master.bind('<Down>', self.turndown)
        self.master.bind('<Left>', self.turnleft)
        self.master.bind('<Right>', self.turnright)
        self.master.bind('<space>', self.obroc)
        self.moving = True
        self.new = False
        self.offsetx = random.randint(2,6)
        self.offsety = 1
        self.start_position = [self.shape[0][0] + self.shape[0][1]*x + self.offsetx + self.offsety, self.shape[1][0] + self.shape[1][1]*x + self.offsetx + self.offsety, self.shape[2][0] + self.shape[2][1]*x + self.offsetx + self.offsety, self.shape[3][0] + self.shape[3][1]*x + self.offsetx + self.offsety]
        self.new_position = [0, 0, 0, 0]
        self.update_position()

    def update_position(self):
        self.new_position = [self.shape[0][0] + self.shape[0][1]*x + self.offsetx + self.offsety*x, self.shape[1][0] + self.shape[1][1]*x + self.offsetx + self.offsety*x, self.shape[2][0] + self.shape[2][1]*x + self.offsetx + self.offsety*x, self.shape[3][0] + self.shape[3][1]*x + self.offsetx + self.offsety*x]

    def check_collision(self, dir):
        if dir == 'down':
            for element in self.new_position:
                if element >= 190 or Canvas.itemcget(square[element + x], "fill") == ground_color:
                    print("true")
                    return True
        elif dir == 'left':
            for element in self.new_position:
                if element % x == 0 or Canvas.itemcget(square[element - 1], "fill") == ground_color:
                    return True
        elif dir == 'right':
            for element in self.new_position:
                if element % x == 9 or Canvas.itemcget(square[element + 1], "fill") == ground_color:
                    return True
        return False

    def move_block(self, direction='fall'):
        if self.moving:
            self.clear_old_position()
            if direction == 'left' and not self.check_collision('left'):
                self.offsetx -= 1
            elif direction == 'right' and not self.check_collision('right'):
                self.offsetx += 1
            elif direction == 'down' or direction == 'fall':
                if not self.check_collision('down'):
                    self.offsety += 1
                else:
                    self.moving = False
            self.update_position()
            self.draw_new_position()
            if not self.moving:
                if self.offsety < 2:
                    finish()
                else:
                    for element2 in self.new_position:
                        Canvas.itemconfig(square[element2], fill=ground_color)
                    check_lines()
                    if not self.new:
                        self.new = True
                        create_block()
                        print("new")
                return
            if direction == 'fall':
                self.master.after(700 - points*10, self.move_block)
            else:
                return

    def turnleft(self, event):
        self.move_block('left')

    def turnright(self, event):
        self.move_block('right')

    def turndown(self, event):
        self.move_block('down')

    def clear_old_position(self):
        for element in self.start_position:
            Canvas.itemconfig(square[element], fill=bg_color)

    def draw_new_position(self):
        for element in self.new_position:
            Canvas.itemconfig(square[element], fill=self.color)
        self.start_position = self.new_position

    def obroc(self, event):
        self.clear_old_position()
        new = []
        for x, y in self.shape:
            new.append((y, -x))
        self.shape = new
        self.update_position()
        self.draw_new_position()


def check_lines():
    for line in range(y):
        to_erase = True
        for block in range(x):
            if Canvas.itemcget(square[line * x + block], "fill") != ground_color:
                to_erase = False
                break
        if to_erase:
            global points
            points += 1
            for line in range(line, 1, -1):
                for q in range(x):
                    Canvas.itemconfig(square[line * x + q], fill=Canvas.itemcget(square[(line - 1) * x + q], "fill"))


def finish():
    messagebox.showinfo("Game Over", "Score: " + str(points))


def create_block():
    k = Block(top)
    k.move_block()


create_block()

Canvas.pack()
top.mainloop()
