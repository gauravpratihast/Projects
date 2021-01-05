# from tkinter import *
# from tkinter import ttk
# import time
#
# root = Tk()
#
# root.title('Testing')
# leftframe = Frame(root)
# leftframe.pack(side=LEFT)
#
# rightframe = Frame(root)
# rightframe.pack(side=RIGHT)
#
# root.geometry('400x400')
#
#
# def step():
#
#     progress.start(10)
#     # time.sleep(2)
#     progress3.start(10)
#     # time.sleep(2)
#     progress4.start(10)
#     # time.sleep(2)
#     progress5.start(10)
#     # time.sleep(2)
#     progress6.start(10)
#     # time.sleep(2)
#     progress7.start(10)
#
#
# progress = ttk.Progressbar(leftframe, orient=VERTICAL, length=100, mode='indeterminate')
# progress6 = ttk.Progressbar(leftframe, orient=VERTICAL, length=100, mode='indeterminate')
# progress3 = ttk.Progressbar(leftframe, orient=VERTICAL, length=100, mode='indeterminate')
# progress4 = ttk.Progressbar(leftframe, orient=VERTICAL, length=100, mode='indeterminate')
# progress5 = ttk.Progressbar(leftframe, orient=VERTICAL, length=100, mode='indeterminate')
# progress7 = ttk.Progressbar(rightframe, orient=VERTICAL, length=100, mode='indeterminate')
#
# progress.pack(side=LEFT, padx=65)
# progress6.pack(side=LEFT)
# progress3.pack(side=LEFT)
# progress4.pack(side=RIGHT)
# progress5.pack(side=RIGHT)
# progress7.pack(side=LEFT, padx=55)
# step()
#
# root.mainloop()


# ---------------------------------------------------------- Infinte loop ball
# import tkinter
# import time
#
# # width of the animation window
# animation_window_width = 800
# # height of the animation window
# animation_window_height = 600
# # initial x position of the ball
# animation_ball_start_xpos = 50
# # initial y position of the ball
# animation_ball_start_ypos = 50
# # radius of the ball
# animation_ball_radius = 30
# # the pixel movement of ball for each iteration
# animation_ball_min_movement = 5
# # delay between successive frames in seconds
# animation_refresh_seconds = 0.01
#
#
# # The main window of the animation
# def create_animation_window():
#     window = tkinter.Tk()
#     window.title("Tkinter Animation Demo")
#     # Uses python 3.6+ string interpolation
#     window.geometry(f'{animation_window_width}x{animation_window_height}')
#     return window
#
#
# # Create a canvas for animation and add it to main window
# def create_animation_canvas(window):
#     canvas = tkinter.Canvas(window)
#     canvas.configure(bg="black")
#     canvas.pack(fill="both", expand=True)
#     return canvas
#
#
# # Create and animate ball in an infinite loop
# def animate_ball(window, canvas, xinc, yinc):
#     ball = canvas.create_oval(animation_ball_start_xpos - animation_ball_radius,
#                               animation_ball_start_ypos - animation_ball_radius,
#                               animation_ball_start_xpos + animation_ball_radius,
#                               animation_ball_start_ypos + animation_ball_radius,
#                               fill="blue", outline="white", width=4)
#     while True:
#         canvas.move(ball, xinc, yinc)
#         window.update()
#         time.sleep(animation_refresh_seconds)
#         ball_pos = canvas.coords(ball)
#         # unpack array to variables
#         xl, yl, xr, yr = ball_pos
#         if xl < abs(xinc) or xr > animation_window_width - abs(xinc):
#             xinc = -xinc
#         if yl < abs(yinc) or yr > animation_window_height - abs(yinc):
#             yinc = -yinc
#
#
# # The actual execution starts here
# animation_window = create_animation_window()
# animation_canvas = create_animation_canvas(animation_window)
# animate_ball(animation_window, animation_canvas, animation_ball_min_movement, animation_ball_min_movement)




# --------------------------------------------------------circle coming from a rectangle in GUI.
# import tkinter as tk
# import random
#
# class Bubble():
#
#     def __init__(self, canvas, x, y, size, color='red'):
#         self.canvas = canvas
#
#         self.x = x
#         self.y = y
#
#         self.start_x = x
#         self.start_y = y
#
#         self.size = size
#         self.color = color
#
#         self.circle = canvas.create_oval([x, y, x+size, y+size], outline=color, fill=color)
#
#     def move(self):
#         x_vel = random.randint(-5, 5)
#         y_vel = -5
#
#         self.canvas.move(self.circle, x_vel, y_vel)
#         coordinates = self.canvas.coords(self.circle)
#
#         self.x = coordinates[0]
#         self.y = coordinates[1]
#
#         # if outside screen move to start position
#         if self.y < -self.size:
#             self.x = self.start_x
#             self.y = self.start_y
#             self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
#
# def move():
#     for item in bubbles:
#         item.move()
#
#     window.after(33, move)
#
# # --- main ---
#
# start_x = 230
# start_y = 270
#
# window = tk.Tk()
# window.geometry("1000x1000")
#
# canvas = tk.Canvas(window, height=1000, width=1000)
# canvas.grid(row=0, column=0, sticky='w')
#
# bubbles = []
# for i in range(5):
#     offset = random.randint(10, 20)
#     b = Bubble(canvas, start_x+10, start_y-offset, 20, 'red')
#     bubbles.append(b)
# for i in range(5):
#     offset = random.randint(0, 10)
#     b = Bubble(canvas, start_x+10, start_y-offset, 20, 'green')
#     bubbles.append(b)
#
# coord = [start_x, start_y, start_x+40, start_y+40]
# rect = canvas.create_rectangle(coord, outline="Blue", fill="Blue")
#
# move()
#
# window.mainloop ()


# -------------------------------------------------------------Magic Matrix
# n = int(input())
# matrix = []
# for i in range(n):
#     nums = input()
#     matrix.append([int(x) for x in nums.split()])
#
# magic = True
# m = [[] for i in range(n)]
# value = sum(matrix[0])
#
# # for rows
# for x, row in enumerate(matrix):
#     if sum(row) != value:
#         magic = False
#
#     for y, element in enumerate(row):
#         m[y].append(element)
#
# # for columns
# for x, column in enumerate(matrix):
#     if sum(column) != value:
#         magic = False
#
# # for diagonal
# i = 0
# j = 0
# diagonal = [[], []]
# for i in range(n):
#     diagonal[0].append(matrix[i][j])
#     diagonal[1].append(matrix[n - 1 - i][j])
#     i += 1
#     j += 1
# if sum(diagonal[0]) != value or sum(diagonal[1]) != value:
#     magic = False
#
# # Output printing
# if magic:
#     print('Magic')
# else:
#     print('Not Magic')
