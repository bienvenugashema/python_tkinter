import tkinter as tk

def click():
    print("I'm clicked")
#create the app

root = tk.Tk()
root.title("My First Tkinter App")

#create a button

btn = tk.Button(root, text="click me", command=click)
btn.pack()
# Create the main window

#inputs

input = tk.Entry(root)
input.pack()

#multi-line text input

text = tk.Text(root, height=15, width=30)
text.pack()


# to create a label

label = tk.Label(root, text="hello my friend")
label.pack()

#to create a Frame

frame = tk.Frame(root, borderwidth=20, relief="groove")
frame.pack()

# Run the application
root.mainloop()