from tkinter import *
from tkinter.ttk import *


root = Tk()
tree = Treeview(root, selectmode="extended", columns=("A", "B"))
tree.pack(expand=YES, fill=BOTH)
tree.heading("#0", text="C/C++ compiler")
tree.column("#0", minwidth=0, width=100, stretch=NO)
tree.heading("A", text="A")
tree.column("A", minwidth=0, width=200, stretch=NO) 
tree.heading("B", text="B")
tree.column("B", minwidth=0, width=300)
root.mainloop()