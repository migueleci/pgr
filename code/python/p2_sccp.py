import Tkinter as tk 
from Tkinter import * 
import tkMessageBox
import tkFileDialog
import subprocess
import datetime

def donothing():
    filewin = Toplevel(root)
    button = Label(filewin, text="En construccion...")
    button.pack()

def maudeParser(str_maude):
	if "result Object:" in str_maude:
		result = str_maude.split("result Object: ")[1]
	else:
		result = str_maude.split("result Configuration: ")[1]
	result = result.replace('\n','').strip()
	# for i in range(len(result)):
	# 	if result[-i]=='>' and result[-i+1]=='M':
	# 		result=result[:-i]
	# 		break	
	while '  ' in result:
		result= result.replace('  ',' ')

	pre_spaces = result.split(" > < ")[:]
	# print(pre_spaces)
	spc_str = ''
	prc_str = ''
	spaces = []
	process = []
	for s in pre_spaces:
		if "store |" in s:
			loc = ((s.split('loc:')[1]).split('>')[0]).replace('(','').replace(')','').strip()
			store = ((s.split('const:')[1]).split(',')[0]).strip()
			while '('in store or ')' in store:
				store=store.replace('(','').replace(')','')
			pre_const = store.split('and')
			const = []
			spc_str += 'space: '+loc+'\nconstraint: '
			for c in pre_const:
				if 'true' not in c:
					const.append(c.strip())
					spc_str += '\n\t'+c.strip()
			spc_str += '\n\n'
			spaces.append([loc,const])

		else: 
			print('process loc',((s.split('loc:')[1]).split('>')[0]).replace('(','').replace(')','').strip())
	return spc_str+prc_str

def showAnswer(maude):
	showAns = Toplevel(root)        
	menuBarA = Menu(showAns)

	fileMenuA = Menu(menuBarA, tearoff=0)
	fileMenuA.add_command(label="Guardar", command=donothing)
	fileMenuA.add_command(label="Cerrar", command=showAns.destroy)
	menuBarA.add_cascade(label="Archivo", menu=fileMenuA)

	solution = Text(showAns)
	solution.insert(END, maudeParser(maude))
	solution.config(relief=GROOVE, borderwidth=2, wrap=tk.WORD, state=DISABLED)
	solution.pack(pady = 20,padx = 20)

	closeAns = Button(showAns, text="Cerrar", command = showAns.destroy)
	closeAns.pack(pady = 10,padx = 10)

	showAns.resizable(width=False, height=False)
	showAns.minsize(width=680, height=500)
	showAns.maxsize(width=680, height=500)
	showAns.config(background='gray', menu=menuBarA)
	showAns.mainloop()


def cmpMaude():
	now = datetime.datetime.now()
	inFileName = '/tmp/' + now.isoformat() + '.in'
	inFile = open(inFileName, 'w')
	inFile.write(editor.get("1.0",END))
	inFile.close()
	
	outFileName = '/tmp/' + now.isoformat() + '.out'
	# print(inFileName,outFileName)
	# print(editor.get("1.0",END))
	try:
		subprocess.check_output("maude.darwin64 maude_code/sccp.maude < "+ inFileName +" > " + outFileName, shell=True)
		outFile = open(outFileName, 'r')		
		ans = outFile.read()
		# editor.delete("1.0",END)
		# editor.insert(END, "\n\n" + ans)
		showAnswer(ans)
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
maudeMenu.add_command(label="Ejecutar", command=cmpMaude)
menuBar.add_cascade(label="Compilar", menu=maudeMenu)

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
compileButton = Button(root, text="Compilar", command = cmpMaude)	# , relief = 'raised')
compileButton.pack()

close = Button(root, text="Cerrar", command = root.quit)
close.pack(pady = 10,padx = 10)

root.title("Spatial Concurrent Constraint Programming")
root.resizable(width=False, height=False)
root.minsize(width=680, height=500)
root.maxsize(width=680, height=500)
root.config(background='gray', menu=menuBar)
root.mainloop()