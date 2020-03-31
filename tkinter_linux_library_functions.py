# coding=utf8
# author: Xose Brais Noya Garcia


#IMPORTS

import sys, os
#from PIL import Image
from tkinter import *
from tkinter import filedialog
#from PIL import ImageTk, Image
#from PIL import ImageTk
import webbrowser
import threading
from tkinter import ttk
from tkinter import messagebox


#GLOBAL VARS
version_software='Simple Debian Cleaner v0.1'
author='Xosé Brais Noya García'
url='https://github.com/xoseng/simpledebiancleaner'
email='xose.noya.garcia@gmail.com'
github='https://github.com/xoseng'

# GUI FUNCTIONS
def about_program():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("About")
    #root.iconbitmap(logo_img)
    #program_directory = sys.path[0]
    #root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "./img/logo_ico.png")))
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=38, height=4, padx=5, pady=5)
    texto.insert(tk.END,version_software+"\nAuthor: "+author+"\nEmail: "+email+"\nGitHub: "+github+"\n")
    texto.config(state="disabled")
    root.mainloop()

def select_warning():
    #messagebox.showinfo('Notice', 'Select at least one option!')
    messagebox.showwarning('Notice', 'Select at least one option!')
    #messagebox.showerror('Notice', 'Select at least one option!')

def info_finish():
    messagebox.showinfo('Notice', 'Work done successfully!')

def license_agreement_gnu():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("license agreement")
    #root.iconbitmap(logo_img)
    program_directory = sys.path[0]
    #root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "./img/logo_ico.png")))
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=77, height=8, padx=5, pady=5)
    texto.insert(tk.END,"GNU General Public License v3.0\n\n"
                        "Permissions of this strong copyleft license are conditioned\n"
                        "on making available complete source code of licensed works and modifications,\n"
                        "which include larger works using a licensed work, under the same license.\n"
                        "Copyright and license notices must be preserved.\n"
                        "Contributors provide an express grant of patent rights.\n")
    texto.config(state="disabled")
    root.mainloop()

def exit_program():
    sys.exit()
    root.destroy()

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def project_website():
    import webbrowser
    webbrowser.open(url)
