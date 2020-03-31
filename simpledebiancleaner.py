# coding=utf8
# author: Xose Brais Noya Garcia
# IMPORTS
#sudo apt-get install python3-pil python3-pil.imagetk
#sudo apt-get install python3-tk
#pyinstaller simpledebiancleaner.py
#cd /media/datos/PycharmProjects/simpledebiancleaner/binaries && /home/xose/.local/bin/pyinstaller /media/datos/PycharmProjects/simpledebiancleaner/simpledebiancleaner.py
#cd /media/datos/PycharmProjects/simpledebiancleaner/binaries && /home/xose/.local/bin/pyinstaller /media/datos/PycharmProjects/simpledebiancleaner/simpledebiancleaner.py --onefile
#/home/xose/.local/bin/pyinstaller /media/datos/PycharmProjects/simpledebiancleaner/binaries/simpledebiancleaner.spec
#cd /media/datos/PycharmProjects/simpledebiancleaner/binaries && /home/xose/.local/bin/pyinstaller -D -F -n main -c /media/datos/PycharmProjects/simpledebiancleaner/simpledebiancleaner.py


import sys, os
import tkinter_linux_library_functions
from tkinter import *
from tkinter import filedialog
import webbrowser
from tkinter import ttk
from tkinter import messagebox


def main_start():

    # NO TK FUNCTIONS
    def clear_vals():
        val_warningselect.set(0)
        val_upgradeos.set(0)
        val_trash.set(0)
        val_thumbnails.set(0)
        val_oldpackages.set(0)
        val_apt.set(0)
        val_unusedpackages.set(0)
        val_webdata.set(0)

    def select_all():
        val_warningselect.set(1)
        val_upgradeos.set(1)
        val_trash.set(1)
        val_thumbnails.set(1)
        val_oldpackages.set(1)
        val_apt.set(1)
        val_unusedpackages.set(1)
        val_webdata.set(1)

    def start_program():
        if val_upgradeos.get() == 1:
            val_warningselect.set(1)
            try:
                os.system("apt update -y && apt upgrade -y")
            except:
                print ("Error to upgrade system")

        if val_trash.get() == 1:
            val_warningselect.set(1)
            try:
                os.system("rm -rf ~/.local/share/Trash/*")
            except:
                print ("Error to delete trash files")

        if val_thumbnails.get() == 1:
            val_warningselect.set(1)
            try:
                os.system("rm -rf ~/.cache/thumbnails/*")
            except:
                print ("Error to delete thumbnails")

        if val_oldpackages.get() == 1:
            val_warningselect.set(1)
            try:
                os.system("apt-get autoclean -y")
            except:
                print("Error to delete old packages")

        if val_unusedpackages.get() == 1:
            val_warningselect.set(1)
            try:
                try:
                    os.system("apt-get autoremove -y")
                except:
                    pass
                try:
                    os.system("apt-get autoremove --purge -y")
                except:
                    pass
            except:
                print("Error to delete unused packages")

        if val_apt.get() == 1:
            val_warningselect.set(1)
            try:
                try:
                    os.system("du -sh /var/cache/apt")
                except:
                    pass
                try:
                    os.system("apt purge -y")
                except:
                    pass
                try:
                    os.system("apt clean -y")
                except:
                    pass
            except:
                print("Error to delete all apt cache and trash")

        if val_webdata.get() == 1:
            val_warningselect.set(1)
            #only works for the next browsers: Mozilla, Chrome and Chromium
            #firefox
            try:
                try:
                    os.system("rm ~/.mozilla/firefox/*.default/cookies.sqlite")
                except:
                    pass
                try:
                    os.system("rm ~/.mozilla/firefox/*.default/*.sqlite ~/.mozilla/firefox/*default/sessionstore.js ;")
                except:
                    pass
                try:
                    os.system("rm -r ~/.cache/mozilla/firefox/*.default/")
                except:
                    pass
            except:
                print ("Error to delete mozilla junk")

            #chrome
            try:
                try:
                    os.system("rm -r ~/.config/google-chrome/Default/")
                except:
                    pass
                try:
                    os.system("rm ~/.cache/google-chrome/*")
                except:
                    pass
            except:
                print ("Error to delete chrome junk")

                # chromium
                try:
                    try:
                        os.system("rm ~/.cache/chromium/Default/Cache/*")
                    except:
                        pass
                    try:
                        os.system("rm ~/.cache/chromium/Default/Media\ Cache/*")
                    except:
                        pass
                except:
                    print("Error to delete chromium junk")

        if val_warningselect.get() == 0:
            tkinter_linux_library_functions.select_warning()

        if val_warningselect.get() == 1:
            tkinter_linux_library_functions.info_finish()
        #restore to default global vals
        clear_vals()

    #MAIN
    version_software = 'Simple Debian Cleaner v0.1'
    logo_path='./img/logo.ico'
    root = Tk()
    root.config(bd=30)
    root.title(version_software)
    #root.iconbitmap(logo_path)

    program_directory = sys.path[0]
    root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "./img/logo_ico.png")))

    #root.geometry("630x250")

    root.resizable(0, 0)  # Disable resize window

    menubar = Menu(root)
    root.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="License agreement", command=tkinter_linux_library_functions.license_agreement_gnu)
    helpmenu.add_command(label="Project website", command=tkinter_linux_library_functions.project_website)
    helpmenu.add_command(label="About", command=tkinter_linux_library_functions.about_program)
    helpmenu.add_command(label="Exit", command=tkinter_linux_library_functions.exit_program)
    menubar.add_cascade(label="Info menu", menu=helpmenu)

    imgpath = './img/logo.png'
    img_tk =PhotoImage(file=imgpath)
    imglabel = Label(root, image=img_tk).grid(row=1, column=1, padx=5, pady=5)

    ######################GLOBAL TK VARS DECLARATION

    val_upgradeos = IntVar(value=0)
    val_trash= IntVar(value=0)
    val_thumbnails= IntVar(value=0)
    val_oldpackages= IntVar(value=0)
    val_apt = IntVar(value=0)
    val_unusedpackages= IntVar(value=0)
    val_webdata=IntVar(value=0)
    val_warningselect=IntVar(value=0)

    #BUTTONS LABEL FORMS...

    Button(root, justify="left", text="SELECT ALL", command=select_all).grid(row=2, column=1, padx=5, pady=5)
    Checkbutton(root, justify="left", text="Upgrade System", variable=val_upgradeos, onvalue=1, offvalue=0).grid(row=3, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="Empty Trash", variable=val_trash, onvalue=1, offvalue=0).grid(row=4, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="Thumbnails Cache ", variable=val_thumbnails, onvalue=1, offvalue=0).grid(row=5, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="APT Cache & Trash ", variable=val_apt, onvalue=1, offvalue=0).grid(row=6, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="Old Version Packages", variable=val_oldpackages, onvalue=1, offvalue=0).grid(row=7, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="Unused Packages", variable=val_unusedpackages, onvalue=1, offvalue=0).grid(row=8, column=1, padx=5, pady=2, sticky='W')
    Checkbutton(root, justify="left", text="Web Browser Data", variable=val_webdata, onvalue=1, offvalue=0).grid(row=9, column=1, padx=5, pady=2, sticky='W')
    Button(root, justify="left", text="START", command=start_program).grid(row=10, column=1, padx=5, pady=5)

    # CENTER WINDOW TO SCREEN
    tkinter_linux_library_functions.center(root)
    # LOOP TK
    root.mainloop()

main_start()