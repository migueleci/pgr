#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import subprocess
import datetime

def say_hi():
    print("hi there, everyone!")

def donothing():
    filewin = Toplevel(root)
    button = Label(filewin, text="En construccion...")
    button.pack()

def maudeParser(str_maude):
    if "result Sys: " in str_maude:
        space = []
        process = []
        sys = (((str_maude.split("result Sys: ")[1]).split("{")[1]).split("}")[0]).replace("\n","")
        while '  ' in sys:
            sys = sys.replace('  ',' ')
        objs = sys.split("[")[1:]
        for obj in objs:
            tmp = (obj.split("]")[0]).split(",")
            if tmp[0] == 'store':
                space.append("Location: {0}\nConstraint: {1}".format(tmp[1],tmp[2]))
            else :
                process.append("Location: {0}\nCommand: {1}".format(tmp[1],tmp[2]))
        space_str ='Spaces:\n'
        for s in space:
            space_str+='\n'+s+'\n'
        
        if len(process)==0:
            return 'Result\n==========================================\n'+space_str

        process_str ='Process:\n'
        for p in process:
            process_str+='\n'+p+'\n'

        return 'Result\n==========================================\n'+space_str+'\n==========================================\n'+process_str
    else :
        return "Sorry, there is an error!\nCheck your specification and try again."

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
    solution.insert(END, maudeParser(maude))
    solution.config(relief=GROOVE, borderwidth=2, wrap=WORD, state=DISABLED, font=customFont_1, width=58, height=16)
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
    
    parserFileName = '/tmp/' + now.isoformat() + '.parser'
    parserFile = open(parserFileName, 'w')
    parserFile.write(editor.get("1.0",END))
    parserFile.close()
    
    inFileName = '/tmp/' + now.isoformat() + '.in'
    
    outFileName = '/tmp/' + now.isoformat() + '.out'
    # print(inFileName,outFileName)
    # print(editor.get("1.0",END))
    # out = subprocess('python3 python/grammar/parser_sccp.py '+parserFileName+' > '+ inFileName, shell=True)

    try:
        subprocess.check_output('python3 python/grammar/parser_sccp.py '+parserFileName+' > '+inFileName, shell=True)
        os = subprocess.check_output("uname -a", shell=True)
        if 'Darwin' in str(os):
            subprocess.check_output("maude.darwin64 maude_code/sccp.maude < "+ inFileName +" > " + outFileName, shell=True)
        else:
            subprocess.check_output("maude.linux64 maude_code/sccp.maude < "+ inFileName +" > " + outFileName, shell=True)
        outFile = open(outFileName, 'r')
        ans = outFile.read()
        # editor.delete("1.0",END)
        # editor.insert(END, "\n\n" + ans)
        showAnswer(ans)
    except:
        # editor.delete("1.0",END)
        editor.insert(END, "\n\nSometing went wrong, please check your input!")
        print("Unexpected error:", sys.exc_info())

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

# Font definition
customFont = font.Font(family='Helvetica', size=18)
customFont_1 = font.Font(family='Avenir Next', size=18)
customFont_2 = font.Font(family='Avenir', size=18)
# print(font.families())

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
editor.config(relief=GROOVE, borderwidth=2, wrap=tk.WORD, font=customFont_1, width=58, height=16)
editor.insert(END, "Insert command here!")
editor.pack(pady = 20,padx = 20)

# Window definition
root.title("Spatial Concurrent Constraint Programming")
root.resizable(width=False, height=False)
root.minsize(width=680, height=500)
root.maxsize(width=680, height=500)
root.config(background='gray', menu=menuBar)
root.mainloop()