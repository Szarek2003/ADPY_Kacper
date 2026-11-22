import random
import tkinter as tk

W, H = 420, 220

root = tk.Tk()
root.title("Ważne pytanie")
root.geometry(f"{W}x{H}")
root.resizable(False, False)
root.attributes("-topmost", True)
root.bind("<Escape>", lambda e: root.destroy())  # awaryjne wyjście

tk.Label(root, text="Czy przyznajesz, że jestem\nnajlepszym kolegą na świecie?",
         font=("Segoe UI", 14, "bold")).place(relx=0.5, y=50, anchor="center")

def tak():
    for w in root.winfo_children():
        w.destroy()
    tk.Label(root, text="Wiedziałem! 😎\n\n(Esc, żeby zamknąć)",
             font=("Segoe UI", 16, "bold"), fg="green").place(relx=0.5, rely=0.5, anchor="center")

btn_tak = tk.Button(root, text="Tak", width=10, command=tak)
btn_tak.place(x=90, y=140)

btn_nie = tk.Button(root, text="Nie", width=10)
btn_nie.place(x=240, y=140)

teksty = ["Nie", "Na pewno?", "Pudło!", "Hehe", "Spróbuj jeszcze", "Nie da rady", "Serio?"]

def uciekaj(event=None):
    bw, bh = btn_nie.winfo_width(), btn_nie.winfo_height()
    x = random.randint(0, W - bw)
    y = random.randint(90, H - bh)
    btn_nie.place(x=x, y=y)
    btn_nie.config(text=random.choice(teksty))

btn_nie.bind("<Enter>", uciekaj)                 # ucieka, gdy najedziesz myszką
btn_nie.config(command=uciekaj)                  # gdyby ktoś trafił Tabem + Enter
root.protocol("WM_DELETE_WINDOW", lambda: None)  # krzyżyk nie działa – tylko Tak albo Esc

root.mainloop()