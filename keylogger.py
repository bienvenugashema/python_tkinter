import tkinter as tk

def key_logger(event):
    print(f"Key pressed: {event.char}")

root = tk.Tk()
root.title("Keylooger")
root.bind("<Key>", key_logger)
root.mainloop()