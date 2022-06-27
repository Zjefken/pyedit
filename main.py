import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
textbox = tk.Text()
textbox.pack()

def printData():
  print('printData called')
  print(textbox.get('1.0','end-1c'))
  root.after(500, printData)

def loadFile():
  print('loadFile called')
  bestand = fd.askopenfilename()
  print(bestand)
  pass

loadButton = tk.Button(text='Laad bestand(naam geschreven)', command=loadFile).pack()
printData()
root.mainloop()