import pywinauto

hwnd = pywinauto.findwindows.find_elements(title="*Untitled - Notepad")

# print(len(hwnd))
# print(hwnd[0]._handle)

if hwnd:
    app = pywinauto.Application().connect(handle=hwnd[0]._handle)
else: app = pywinauto.Application().start("Notepad.exe")
# app = pywinauto.Application().connect(title_re="*Untitled - Notepad")
np = app.UntitledNotepad
np.edit.type_keys("hello")
