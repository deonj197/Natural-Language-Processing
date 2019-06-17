from NLTK_Features.Sentiment import *

def Stats_Menu_Gui(window2):
    window2.withdraw()

    #Initialize third frame (analytucs menu gui)
    window3 = Tk()
    window3.geometry("1200x500")
    window3.title("ANALYTICS Menu")

    #Freq
    label = Label(window3, text="Choose an option from the ANALYTICS menu: ",font=("Times New Roman Bold Italic", 40),foreground= "green")
    label.grid(column=0, row=0)    

    def local():
           freq_Dist()
                      
    #LFrequency Distribution
    option1Button = Button(window3, text= "Frequency Distribution", bg="light blue", fg="black", command = local)
    option1Button.config(height = 1, width = 20)
    option1Button.grid(pady=15)

    def local2():
        stop_words()
        
    #Stop Words
    option2Button = Button(window3, text= "Stop Words", bg="light blue", fg="black", command = local2)
    option2Button.config(height = 1, width = 20)
    option2Button.grid(pady=15)

    def local3():
        stemming()
        
    option3Button = Button(window3, text = "Stemming", bg = "light blue", fg = "black", command = local3)
    option3Button.config(height = 1, width = 20)
    option3Button.grid(pady = 15)

    def local4():
        sentiment_analysis()
    option4Button = Button(window3, text = 'Sentiment Analysis', bg = 'light blue', fg = 'black', command = local4)
    option4Button.config(height = 1, width = 20)
    option4Button.grid(pady = 15)

    def local5():
        sentece_word_tag()
    option5Button = Button(window3, text = 'Word Tagging', bg = 'light blue', fg = 'black', command = local5)
    option5Button.config(height = 1, width = 20)
    option5Button.grid(pady = 15)

    def local6():
        Synonym_analysis()
    option5Button = Button(window3, text = 'Synonym Analysis', bg = 'light blue', fg = 'black', command = local6)
    option5Button.config(height = 1, width = 20)
    option5Button.grid(pady = 15)
    
        
    def quite():
        window3.destroy()
        window2.deiconify()

    goBackBtn = Button(window3, text="Go Back",bg="light blue", fg="black", command = quite)
    goBackBtn.grid(pady=15)   
    window3.mainloop()
    
    
#Gui for Minor menu, we pass in the old frame so we can get to it again in case we need to go back        
def Minor_Menu_Gui(window):
        #Hide main frame
        window.withdraw()

        #Initialize second frame (minor menu gui)
        window2 = Tk()
        window2.geometry("800x500")
        window2.title("Minor Menu")
        
        label = Label(window2, text="Choose an option from the menu: ",font=("Times New Roman Bold Italic", 40),foreground= "green")
        label.grid(column=0, row=0)

        def local():
           read_text()
            
            
        #Local file
        option1Button = Button(window2, text= "Access Local", bg="light blue", fg="black", command = local)
        option1Button.config(height = 1, width = 20)
        option1Button.grid(pady=15)

        def local2():
            read_from_web()
            
        #WEB
        option2Button = Button(window2, text= "Access Web", bg="light blue", fg="black", command = local2)
        option2Button.config(height = 1, width = 20)
        option2Button.grid(pady=15)
            
        #ANALYTICS MENU
        option3Button = Button(window2, text= "Access Analytics Menu", bg="light blue", fg="black",command=  lambda: Stats_Menu_Gui(window2))
        option3Button.config(height = 1, width = 20)
        option3Button.grid(pady=15)

        def quite():
            window2.destroy()
            window.deiconify()
            
        goBackBtn = Button(window2, text="Go Back",bg="light blue", fg="black", command = quite)
        goBackBtn.grid(pady=15)

        
        window2.mainloop()
#First Menu        
def gui_menu():
    #library
    import tkinter

    #define window from
    window = Tk()

    #name of frame
    window.title("HOME PAGE")

    #dimensions
    window.geometry('1000x650+0+0')

    #text (label + position)
    lbl = Label(window, text="Welcome to UMD ANALYTICS!", font=("Times New Roman Bold Italic", 50), foreground= "blue")
    lbl.grid(column=0, row=0)

    #Access File button
    #opens other Minor Menu GUI, we pass the current GUI (window), so as to open it later on through hide & show 
    option1Button = Button(window, text= "Access Corpora", bg="light blue", fg="black", command=  lambda: Minor_Menu_Gui(window))
    option1Button.grid(pady=15)

    #Message Box (confirm exit)
    def message_Box():
        from tkinter import messagebox
        result = messagebox.askyesno('Exit Program','Are you sure you want to Exit?')
        if(result == True):
            quit()
            
    #close window
    #close PROGRAM (like every file associated w/ program!)
    def quit():     
       window.destroy()
       import os
       os.system("taskkill /f /im pythonw.exe")
    
    #Exit Program Button
    option2Button = Button(window, text= "Exit Program     ", bg="light blue", fg="black",command=message_Box)
    option2Button.grid(pady=15)    
    
    #start window frame
    window.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import ttk

import tkinter.scrolledtext as tkst

def createWidgets():
    
    win = Tk()
    win.geometry('1000x650+0+0')
    tabControl = ttk.Notebook(win)
    
    tab1 = ttk.Frame(tabControl)            
    tabControl.add(tab1, text='Tab 1')

    tab2 = ttk.Frame(tabControl)   
    tabControl.add(tab2, text='Tab 2')
    
    tabControl.pack(expand=10, fill="both")
    
    monty = ttk.LabelFrame(tab1, text=' Monty Python ')
    monty.grid(column=0, row=0, padx=8, pady=4)

    monty2 = ttk.LabelFrame(tab2, text=' Monty2 Python ')
    monty2.grid(column=0, row=0, padx=8, pady=4)

    scr = tkst.ScrolledText(monty, width=30, height=3, wrap=tk.WORD)
    scr.grid(column=0, row=3, sticky='WE', columnspan=3)

    scr2 = tkst.ScrolledText(monty2, width=30, height=3, wrap=tk.WORD)
    scr2.grid(column=0, row=3, sticky='WE', columnspan=3)

    
    win.mainloop()
    
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
def demo():
    root = tk.Tk()
    root.title("ttk.Notebook")
    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb)

    monty = ttk.LabelFrame(page1, text=' Monty Python ')
    monty.grid(column=0, row=0, padx=8, pady=4)

    scr = tkst.ScrolledText(monty, width=100, height=100, wrap=tk.WORD)
    scr.grid(column=0, row=3, sticky='WE', columnspan=3)

    # second page
    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    
    text.pack(expand=1, fill="both")
    
    nb.add(page1, text='One')
    nb.add(page2, text='Two')

    nb.pack(expand=1, fill="both")
    
    root.mainloop()      
