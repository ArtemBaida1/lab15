import tkinter as tk
import numpy as np

def solve_system():
    try:
        a1, b1, c1, d1 = float(entries[0].get()), float(entries[1].get()), float(entries[2].get()), float(entries[3].get())
        a2, b2, c2, d2 = float(entries[4].get()), float(entries[5].get()), float(entries[6].get()), float(entries[7].get())
        a3, b3, c3, d3 = float(entries[8].get()), float(entries[9].get()), float(entries[10].get()), float(entries[11].get())

        A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        B = np.array([d1, d2, d3])

        solution = np.linalg.solve(A, B)
        result_label.config(text=f"Розв'язок: x = {solution[0]:.2f}, y = {solution[1]:.2f}, z = {solution[2]:.2f}")
    except Exception as e:
        result_label.config(text="Помилка: Невірні дані або система не має розв'язку")

root = tk.Tk()
root.geometry("430x200")
root.title("Розв'язання системи рівнянь третього порядку")

entries = []
labels = ["a", "b", "c", "d"]

for i in range(3):
    for j in range(4):
        label_text = f"{labels[j]}{i+1}"
        tk.Label(root, text=label_text).grid(row=i*2, column=j*2, padx=5, pady=5, sticky="e")
        entry = tk.Entry(root, width=10)
        entry.grid(row=i*2, column=j*2 + 1, padx=5, pady=5)
        entries.append(entry)

solve_button = tk.Button(root, text="Розв'язати", command=solve_system)
solve_button.grid(row=6, column=0, columnspan=8, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=7, column=0, columnspan=8, pady=10)

root.mainloop()