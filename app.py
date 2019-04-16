#!/usr/bin/python3

from modules.cell import Cell
from modules.world import World
from modules.gui import Gui
import numpy as np
import tkinter as tk
import PIL
import PIL.Image, PIL.ImageTk
import cv2 as cv

world = World(
    {
        Cell(0, 0, 'B'),
        Cell(1, 1, 'B'),
        Cell(1, 2, 'B'),
        Cell(0, 2, 'B'),
        Cell(-1, 2, 'B'),

        Cell(4, 5, 'C'),
        Cell(4, 4, 'C'),
        Cell(2, 4, 'C'),
        Cell(3, 4, 'C'),

        Cell(-1, -1, 'A'),
        Cell(-2, -1, 'A'),
        Cell(0, -1, 'A'),

        Cell(-3, -1, 'D'),
        Cell(-4, -1, 'D'),
        Cell(-5, -1, 'D'),
        Cell(-6, -1, 'D'),

        # Cell(-0, -5, 'A'),
        # Cell(-7, -1, 'A'),
        })
gui = Gui(20)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.textX1.insert(0,'0')
        self.textX2.insert(0,'0')
        self.textY1.insert(0,'0')
        self.textY2.insert(0,'0')

    def create_widgets(self):
        self.field = np.zeros((400, 400, 3), dtype=np.uint8)
        height, width, channels = self.field.shape

        # interface
        self.frame2=tk.Frame(self,width=200,height=400)
        self.frame2.grid(row=0, column=1)

        # ширина поляв клетках
        self.textX1=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textX1.place(x='0', y='0')
        self.labelX1=tk.Label(self.frame2,text='X1',font='Arial 14')
        self.labelX1.place(x='170', y='0')

        # высота поляв клетках
        self.textY1=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textY1.place(x='0', y='50')
        self.labelY1=tk.Label(self.frame2,text='Y1',font='Arial 14')
        self.labelY1.place(x='170', y='50')

        
        self.textX2=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textX2.place(x='0', y='100')
        self.labelX2=tk.Label(self.frame2,text='X2',font='Arial 14')
        self.labelX2.place(x='170', y='100')

        # смещение по вертикали
        self.textY2=tk.Entry(self.frame2,width=10,font='Arial 14')
        self.textY2.place(x='0', y='150')
        self.labelY2=tk.Label(self.frame2,text='Y2',font='Arial 14')
        self.labelY2.place(x='170', y='150')

        self.quit = tk.Button(
            self.frame2, text='next', fg="red", width='22',
            command=self.next)
        self.quit.place(x='0', y='350')

    def update_borders(self):
        max_x = int(self.textX1.get())
        max_y = int(self.textY1.get())
        root_x = int(self.textX2.get())
        root_y = int(self.textY2.get())

    def next(self, root_mode=True):
        print("hi there, everyone!")
        if (root_mode):
            root.update()

        self.update_borders()

        gui.set_args(10, 10, max_x, max_y, root_x, root_y)
        gui.draw(world)
        world.next_state()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
i = 0
