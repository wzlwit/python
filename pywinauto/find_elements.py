import pywinauto

app = pywinauto.Application().connect(title_re='.*Notepad',class_name="Notepad")

# app.hellotxtNotepad.menu_select("help->About Notpad")

