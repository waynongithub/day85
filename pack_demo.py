import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

mainframe = tk.Frame(root, bg='lime')
footer = tk.Frame(root)
label1 = tk.Label(master=mainframe, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=mainframe,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=mainframe, text='Demo',bg='blue', fg='white')
label4 = tk.Label(master=footer, text='Demo',bg='yellow', fg='white')

label1.pack(side='top', expand=False)
label2.pack(side='top', expand=True)
label3.pack(side='top', expand=False)
# footer is a container that allows label4 to be placed bottom right
mainframe.pack(side='top', expand=True, fill=tk.Y)
footer.pack(side='bottom', expand=False, fill=tk.X)
label4.pack(anchor=tk.SE, padx=5, pady=5)
# label4.grid(row=0, column=0, anchor=tk.E)
root.mainloop()