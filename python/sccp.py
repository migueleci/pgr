import Tkinter as tk 
from Tkinter import * 
import tkMessageBox
import tkFileDialog
import subprocess
import datetime

def compile():
	now = datetime.datetime.now()
	inFileName = '/tmp/' + now.isoformat() + '.in'
	inFile = open(inFileName, 'w')
	inFile.write(editor.get("1.0",END))
	inFile.close()
	
	outFileName = '/tmp/' + now.isoformat() + '.out'
	print(inFileName,outFileName)
	print(editor.get("1.0",END))
	try:
		subprocess.check_output("maude.darwin64 maude_code/sccp.maude < "+ inFileName +" > " + outFileName, shell=True)
		outFile = open(outFileName, 'r')		
		ans = outFile.read()
		# editor.delete("1.0",END)
		editor.insert(END, "\n\n" + ans)
	except:
		# editor.delete("1.0",END)
		editor.insert(END, "\n\nSometing went wrong, please check your input!")

def openFile():
	path = subprocess.check_output("pwd",shell=True)
	file_opt = options = {}
	options['initialdir'] = path
	options['parent'] = root
	options['filetypes'] = [('Plain text', '*.txt'),('Maude', '*.maude'),('Input', '*.in')]
	options['title'] = 'Select specification source'
	file = tkFileDialog.askopenfile(mode='r', **file_opt)
	if file is None:
		return
	editor.delete("1.0",END)
	spec = file.read()
	editor.insert(END, spec)

def saveFile():
	path = subprocess.check_output("pwd",shell=True)
	file_opt = options = {}
	options['initialdir'] = path
	options['parent'] = root
	options['defaultextension'] = '.in'
	options['filetypes'] = [('Plain text', '*.txt'),('Maude', '*.maude'),('Input', '*.in')]
	options['title'] = 'Save specification as ...'
	file = tkFileDialog.asksaveasfile(mode='w', **file_opt)
	if file is None:
		return
	spec = editor.get("1.0",END)
	file.write(spec)
	file.close()

def donothing():
    filewin = Toplevel(root)
    button = Label(filewin, text="En construccion...")
    button.pack()


# Window definition
root = Tk()

# Top menu definition
menuBar = Menu(root)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Abrir", command=openFile)
fileMenu.add_command(label="Guardar", command=saveFile)
fileMenu.add_command(label="Cerrar", command=root.quit)
menuBar.add_cascade(label="Archivo", menu=fileMenu)

maudeMenu = Menu(menuBar, tearoff=0)
maudeMenu.add_command(label="Ejecutar", command=donothing)
menuBar.add_cascade(label="Maude", menu=maudeMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=donothing)
helpMenu.add_command(label="Acerca de...", command=donothing)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

# Text editor definition
editor = Text(root)
editor.config(relief=GROOVE, borderwidth=2, wrap=tk.WORD)
editor.insert(END, "Insert command here!")
editor.pack(pady = 20,padx = 20)

# Buttons definition
compileButton = Button(root, text="Compilar", command = compile)	# , relief = 'raised')
compileButton.pack()

root.title("Spatial Concurrent Constraint Programming")
root.resizable(width=False, height=False)
root.minsize(width=666, height=666)
root.config(background='gray', menu=menuBar)
root.mainloop()
