from tkinter import *


class Pen(Canvas):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.fill = 'red'
        self.prex = self.prey = -10
        self.create_dot = False
        self.bind('<B1-Motion>', self.move)
        self.bind('<Button-1>', self.start)
        self.bind('<ButtonRelease-1>', self.end)
        self.bind('<Button-3>', self.clean)
        self.pack(fill=BOTH, expand=YES)

    def start(self, event):
        self.create_dot = True
        if event.x > 0 and event.y >0:
            self.master['cursor'] = 'target'

    def move(self, event):
        if self.prex > 0 and self.prey > 0 and self.create_dot == True:
            self.create_line(self.prex, self.prey, event.x, event.y, width=5)
        self.prex, self.prey = event.x, event.y

    def end(self, event):
        self.create_dot = False
        self.master['cursor'] = 'arrow'
        self.prex = self.prey = -10

    def clean(self, event):
        self.delete('all')
        self.prex = self.prey = -10

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    root.resizable(width=False, height=False)
    root.title('画画')
    p = Pen(root)
    root.mainloop()