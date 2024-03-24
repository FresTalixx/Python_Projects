import tkinter as tk

root = tk.Tk()

root.title("Програма")

root.geometry("640x480")

label = tk.Label(root, text="Стрічка", font=("Arial", 35), background="Red")
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 17))
textbox.pack()
root.mainloop()
