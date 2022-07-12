import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
textbox = tk.Text()
textbox.pack()
file = None

def loadFile():
  global file
  file = fd.askopenfilename()
  with open(file, 'rb') as fileRead:
    content = fileRead.read()
    textbox.delete('1.0','end-1c')
    textbox.insert('1.0', content)

def saveFile():
  global file
  if file == None:
    file = fd.askopenfilename()
  with open(file, 'wb') as fileWrite:
    fileWrite.write(textbox.get('1.0','end-1c').encode('utf-8'))

loadButton = tk.Button(text='Load file', command=loadFile).pack()
saveButton = tk.Button(text='Save file', command=saveFile).pack()
root.mainloop()