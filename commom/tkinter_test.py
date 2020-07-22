from tkinter import *

# root = Tk()
# list1 = ['you', 'me', 'she', 'he']
# list2 = ['你', '我', '她', '他']
# listb = Listbox(root)
# listb2 = Listbox(root)
# for i in list1:
#     listb.insert(len(list1), i)
# for i in list2:
#     listb2.insert(len(list2), i)
# listb.pack()
# listb2.pack()
# root.mainloop()
init_window = Tk()
init_window.title('test窗口')
init_window.geometry('700x500')
in_data_label = Label(init_window, text='输入数据')
in_data_label.grid(row=0, column=0)
out_data_label = Label(init_window, text='输出数据')
out_data_label.grid(row=0, column=10)
in_data_text = Text(init_window, width=50, height=20)
in_data_text.grid(row=1, column=0, rowspan=12, columnspan=10)
out_data_text = Text(init_window, width=50, height=20)
out_data_text.grid(row=1, column=10, rowspan=12, columnspan=10)
def adddata(data1, data2):
    data2.insert(1.0, data1)
data1 = in_data_text.get(1.0, END)
data_button = Button(init_window, text='计算', width=15, command=adddata(data1, out_data_text))
data_button.grid(row=20, column=10)
init_window.mainloop()