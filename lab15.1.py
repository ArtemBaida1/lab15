import tkinter as tk
from tkinter import Text, filedialog

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, text_content)

root = tk.Tk()
root.geometry("600x350")
root.configure(bg="blue")

text_widget = Text(root, wrap="word", bg="white", fg="black")
text_widget.place(x=10, y=10, width=580, height=300)

load_button = tk.Button(root, text="Завантажити файл", command=load_file)
load_button.place(x=250, y=320)

root.mainloop()
