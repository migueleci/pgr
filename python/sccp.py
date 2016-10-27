from Tkinter import *
from tkFileDialog import askopenfilename
import subprocess
import time
import sys
import StringIO

def test():
	global labelA
	try: 
		subprocess.check_output("maude.darwin64 maude_code/sccp.maude < maude_code/examples.sccp.in > maude_code/examples.sccp.out",shell=True)
		labelA["text"] = "OK"
	except:
		labelA["text"] = "Someting went wrong, please check your input!"



def setWindow():
	global frame, label, tk, labelA
	frame = Frame(tk)
	frame.pack(fill=X)
	#canvas = Canvas(frame, bg="grey", width=600, height=600)
	#canvas.pack()
	label = Label(frame, width=30, height=1)
	label.pack()
	audioS = Button(frame, text="Test", command=test)
	audioS.pack()
	labelA = Label(frame, text="Waiting", width=30, height=3)
	labelA.pack()
	
	quit = Button(frame, text="QUIT", fg="red", command=tk.destroy)
	quit.pack(side="bottom")

	labelC = Label(frame, width=30, height=3)
	labelC.pack()

def main():
	global tk
	tk = Tk()
	tk.title("Spatial Concurrent Constraint Programming")
	# tk.maxsize(1000, 400)
	setWindow()
	tk.mainloop()

main()