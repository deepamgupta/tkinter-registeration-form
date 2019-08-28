import tkinter as tk

def clicked():
    res =  "Welcome " + txt.get()
    label.configure(text= res, fg="blue")
    combo_lbl.configure(text=combo.get())
    chk_lbl.configure(text="Choosen" if chk_state.get() else "Not Choosen")

root = tk.Tk()
root.title("Hello World!!")
# root.geometry("700x300")
btn = tk.Button(root, text="Quit",height=2, command=root.destroy, bg="red", fg="pink", font=("Verdana", 20))

btn.grid(row=0, column =0)

btn2 = tk.Button(root, text="Click Me!!", height=2, command=clicked, bg="blue", fg="orange", font=("Impact", 50))
btn2.grid(row = 0, column=1)

label = tk.Label(root, text="This is a label!!", height=2, font=("Comic Sans MS", 20))
label.grid(row=0, column=2)

txt = tk.Entry(root)
# txt.insert(0, "Enter your name")
txt.grid(row=1, column=0)
txt.focus()


from tkinter import ttk

combo = ttk.Combobox(root)
combo['values'] = (1, "hi", 0xABCD, 401)
combo.current(1) #set the selected index
combo.grid(row = 1, column= 1)
combo_lbl = tk.Label(root, text="ComboValue", font=("Impact", 15))
combo_lbl.grid(row = 1, column = 2)

chk_state = tk.BooleanVar()
chk_state.set(False)
chk = tk.Checkbutton(text="Choose", variable=chk_state, command=clicked)
chk.grid(row = 2, column=0)
chk_lbl = tk.Label(root, text="Choosen" if chk_state.get() else "Not Choosen", font=("Courier New", 15))
chk_lbl.grid(row = 2, column = 1)

def gender_click():
    rad_lbl.configure(text=selected.get())

selected = tk.StringVar()
rad1 = tk.Radiobutton(root, text="Male", value="male", variable=selected, command=gender_click)
rad1.grid(row=3, column=0)
rad2 = tk.Radiobutton(root, text="Female", value="female", variable=selected, command=gender_click)
rad2.grid(row=3, column=1)

rad_lbl = tk.Label(text="Gender")
rad_lbl.grid(row= 3, column = 2)


from tkinter import messagebox
messagebox.showwarning('Message title', 'Message content')
messagebox.showerror('Message title', 'Message content')    #shows error message

res = messagebox.askquestion('Message title', 'Message content')

res = messagebox.askyesno('Message title', 'Message content')

res = messagebox.askyesnocancel('Message title', 'Message content')

res = messagebox.askokcancel('Message title', 'Message content')

res = messagebox.askretrycancel('Message title', 'Message content')

root.mainloop()

