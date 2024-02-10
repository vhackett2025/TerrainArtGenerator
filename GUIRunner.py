import tkinter as tk

root = tk.Tk()
root.title('Terrain Art Generator')
root.geometry("900x600")

parameter_label = tk.Label(root, text = "Parameters")
parameter_label.config(font =("Courier", 14))
parameter_label.pack(pady=5, side= tk.TOP, anchor="w")

generate_button = tk.Button(root, text='Test', width=25, command=root.destroy)
generate_button.pack()

root.mainloop()