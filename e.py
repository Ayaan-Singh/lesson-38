from tkinter import *
window = Tk()
window.title("HI")
window.geometry('350x200')
def handle_keypress(event):
    print("key was pressed")
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("The button was clicked!")
button = Button(window, text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)
mainloop()
