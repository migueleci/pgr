import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import datetime

def say_hi():
    print("hi there, everyone!")

def donothing():
    filewin = Toplevel(root)
    button = Label(filewin, text="En construccion...")
    button.pack()

def showAnswer(maude):
    def saveFileOuput():
        path = subprocess.check_output("pwd",shell=True)
        file_opt = options = {}
        options['initialdir'] = path
        options['parent'] = showAns
        options['defaultextension'] = '.out'
        options['filetypes'] = [('Plain text', '*.txt'),('Maude', '*.maude'),('Output', '*.out')]
        options['title'] = 'Save solution as ...'
        file = filedialog.asksaveasfile(mode='w', **file_opt)
        if file is None:
            return
        text = solution.get("1.0",END)
        file.write(text)
        file.close()

    showAns = Toplevel(root)
    menuBarA = Menu(showAns)

    fileMenuA = Menu(menuBarA, tearoff=0)
    fileMenuA.add_command(label="Guardar", command=donothing)
    fileMenuA.add_separator()
    fileMenuA.add_command(label="Cerrar", command=showAns.destroy)
    menuBarA.add_cascade(label="Archivo", menu=fileMenuA)

    solution = Text(showAns)
    solution.insert(END, maude)
    solution.config(relief=GROOVE, borderwidth=2, wrap=WORD, state=DISABLED)
    solution.pack(pady = 20,padx = 20)

    # Top toolbar definiton
    toolbarAns = Frame(showAns, bd=1, relief=RAISED)

    saveImgAns = PhotoImage(file="python/icon/save2.gif")  
    saveImgAns = saveImgAns.subsample(20)
    saveButtonAns = Button(toolbarAns, image=saveImgAns, relief=FLAT, command=saveFileOuput)
    saveButtonAns.image = saveImgAns
    saveButtonAns.pack(side=LEFT, padx=2, pady=2)
    
    quitEimgAns = PhotoImage(file="python/icon/exit.gif")  
    quitEimgAns = quitEimgAns.subsample(20)
    quitButtonAns = Button(toolbarAns, image=quitEimgAns, relief=FLAT, command=showAns.destroy)
    quitButtonAns.image = quitEimgAns
    quitButtonAns.pack(side=RIGHT, padx=2, pady=2)

    toolbarAns.pack(side=BOTTOM, fill=X)

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
    file = filedialog.askopenfile(mode='r', **file_opt)
    if file is None:
        return
    editor.delete("1.0",END)
    spec = file.read()
    editor.insert(END, spec)

def saveFileInput():
    path = subprocess.check_output("pwd",shell=True)
    file_opt = options = {}
    options['initialdir'] = path
    options['parent'] = root
    options['defaultextension'] = '.in'
    options['filetypes'] = [('Plain text', '*.txt'),('Maude', '*.maude'),('Input', '*.in')]
    options['title'] = 'Save specification as ...'
    file = filedialog.asksaveasfile(mode='w', **file_opt)
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
fileMenu.add_command(label="Guardar", command=saveFileInput)
fileMenu.add_separator()
fileMenu.add_command(label="Cerrar", command=root.destroy)
menuBar.add_cascade(label="Archivo", menu=fileMenu)

maudeMenu = Menu(menuBar, tearoff=0)
maudeMenu.add_command(label="Ejecutar", command=cmpMaude)
menuBar.add_cascade(label="Compilar", menu=maudeMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=donothing)
helpMenu.add_command(label="Acerca de...", command=donothing)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

# Top toolbar definiton
toolbar = Frame(root, bd=1, relief=RAISED)

openImg = PhotoImage(file="python/icon/open1.gif")  
openImg = openImg.subsample(20)
openButton = Button(toolbar, image=openImg, relief=FLAT, command=openFile)
openButton.image = openImg
openButton.pack(side=LEFT, padx=2, pady=2)

saveImg = PhotoImage(file="python/icon/save2.gif")  
saveImg = saveImg.subsample(20)
saveButton = Button(toolbar, image=saveImg, relief=FLAT, command=saveFileInput)
saveButton.image = saveImg
saveButton.pack(side=LEFT, padx=2, pady=2)

compImg = PhotoImage(file="python/icon/compile.gif")  
compImg = compImg.subsample(20)
compButton = Button(toolbar, image=compImg, relief=FLAT, command=cmpMaude)
compButton.image = compImg
compButton.pack(side=LEFT, padx=2, pady=2)

quitEimg = PhotoImage(file="python/icon/exit.gif")  
quitEimg = quitEimg.subsample(20)
quitButton = Button(toolbar, image=quitEimg, relief=FLAT, command=root.destroy)
quitButton.image = quitEimg
quitButton.pack(side=RIGHT, padx=2, pady=2)

toolbar.pack(side=BOTTOM, fill=X)

# Text editor definition
editor = Text(root)#, width=450, height=300)
editor.config(relief=GROOVE, borderwidth=2, wrap=tk.WORD)
editor.insert(END, "Insert command here!")
editor.pack(pady = 20,padx = 20)

# Window definition
root.title("Spatial Concurrent Constraint Programming")
root.resizable(width=False, height=False)
root.minsize(width=680, height=500)
root.maxsize(width=680, height=500)
root.config(background='gray', menu=menuBar)
root.mainloop()