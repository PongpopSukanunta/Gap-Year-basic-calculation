from tkinter import *
from tkinter import ttk, messagebox
from math import pi

def calculate():
	input1 = value1.get()
	input2 = value2.get()
	res = input1 + input2
	result.set(f'คำตอบ: {res:,d}')


def add():
	messagebox.showinfo(title='วิธีบวก', message='ตัวอย่าง 1 + 1 = 2')


def areaCircle():
	r = radius.get()
	answer = pi * r ** 2
	ans.set(f'รัศมี {r} จะได้พื้นที่เท่ากับ {answer:,.2f}')


def new_win():
	GUI2 = Toplevel()
	GUI2.title('New Window')
	GUI2.geometry('300x300')
	L1 = Label(GUI2, text='New Window!', font=FONT1)
	L1.pack(pady=130)

	GUI2.mainloop()


GUI = Tk()

GUI.title('Calculate Program')
GUI.geometry('500x600')

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)

F1 = Frame(Tab)
F2 = Frame(Tab)

Tab.add(F1, text='พื้นฐานการคำนวน')
Tab.add(F2, text='วงกลม')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar, tearoff=0)
file.add_command(label='Close', command=GUI.quit)
file.add_command(label='New file', command=new_win)
menubar.add_cascade(label='File', menu=file)

tools = Menu(menubar, tearoff=0)
tools.add_command(label='add', command=add)
tools.add_command(label='subtract')
tools.add_command(label='multiply')
tools.add_command(label='divide')
menubar.add_cascade(label='Tools', menu=tools)

FONT1 = ('Courier New', 18)
FONT2 = ('Angsana New', 18)

# Frame 1 คำนวน
L1 = Label(F1, text='โปรมแกรมคำนวน', font=FONT1)
L1.pack(pady=50)

value1 = IntVar()
value2 = IntVar()
result = IntVar()
result.set('-----')

E1 = ttk.Entry(F1, textvariable=value1, font=FONT2)
E1.pack(ipady=30, ipadx=50)

E2 = ttk.Entry(F1, textvariable=value2, font=FONT2)
E2.pack(ipady=30, ipadx=50, pady=50)

B1 = ttk.Button(F1, text='คำนวน', command=calculate)
B1.pack()

LResult = ttk.Label(F1, textvariable=result, font=FONT2)
LResult.pack(pady=5)

# Frame 2 วงกลม
L2 = Label(F2, text='คำนวนพื้นที่วงกลม', font=FONT1)
L2.pack(pady=50)

radius = IntVar()
ans  = StringVar()
ans.set('------')

E3 = Entry(F2, textvariable=radius, font=FONT2)
E3.pack(ipady=30, ipadx=50)

B2 = ttk.Button(F2, text='คำนวน', command=areaCircle)
B2.pack(pady=30)

LResult2 = ttk.Label(F2, textvariable=ans, font=FONT2)
LResult2.pack()

GUI.mainloop()
