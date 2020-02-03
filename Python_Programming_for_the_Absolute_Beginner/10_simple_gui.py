# create the root window
root = Tk()

# modify the window
root.title("Simple GUI")
root.geometry("200x100")

# create a frame in the window to hold other widgets
app = Frame(root)
# associate with a layout manager
app.grid()

# create a label in the frame
lbl = Label(app, text = "I'm a label!")
# ensure the label will be visible
lbl.grid()

# create a button in the frame
bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()

# create a second button in the frame
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")

# create a third button in the frame
bttn3 = Button(app)
bttn3.grid()
#* configure a control via Dict
bttn3[“text”] = "Same here!"


# kick off the window's event loop
root.mainloop()

