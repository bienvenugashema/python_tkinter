import tkinter as tk

# Start gui
root = tk.Tk()
root.title("Simple form")
def add_user():
    print(f"Name is : {name.get()}")
    print(f"Email is : {email.get()}")
# form for entering information in the forms
#labels
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Email:").grid(row=1, column=0)
name = tk.Entry(root)
name.grid(row=0,column=1)
email = tk.Entry(root)
email.grid(row=1, column=1)


submit_btn = tk.Button(root, text="Add user", command=add_user).grid(row=3, column=0)

root.mainloop()