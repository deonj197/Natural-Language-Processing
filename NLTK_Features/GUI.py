from NLTK_Features.Sentiment import *
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter.scrolledtext import ScrolledText

#************************* WINDOW 1 *************************       
def gui_menu():
    #define window from
    window = Tk()
    #name of frame
    window.title("HOME PAGE")
    #dimensions
    window.geometry('360x170+0+0')
    
    # Positioning the Window
    window.withdraw()
    window.update_idletasks()  # Update "requested size" from geometry manager
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
    window.geometry("+%d+%d" % (x-110, y-20))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    window.deiconify()
    
    window.configure(bg='gray86')

    #text (label + position)
    lbl = Label(window, text="UMD ANALYTICS!", font=("Arial Bold Italic", 30), foreground= "dodgerblue3", bg = 'gray86')
    lbl.grid(column=0, row=0)

    #Access File button
    #opens other Minor Menu GUI, we pass the current GUI (window), so as to open it later on through hide & show 
    option1Button = Button(window, text= "Access Corpora", bg="skyblue2", fg="black", command=  lambda: Minor_Menu_Gui(window))
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
    option2Button = Button(window, text= "Exit Program     ", bg="skyblue2", fg="black", command=message_Box)
    option2Button.grid(pady=15)    
    
    #start window frame
    window.mainloop()
#******************************END WINDOW 1****************************

    
#Gui for Minor menu, we pass in the old frame so we can get to it again in case we need to go back

### ***************************WINDOW #2*********************************
    
def Minor_Menu_Gui(window):
        #Hide main frame
        window.withdraw()
        
        #Initialize second frame (minor menu gui)
        window2 = Tk()
        window2.geometry("430x280")
        window2.title("Minor Menu")
        window2.configure(bg='gray86')
        
        # Positioning the Window
        window2.update_idletasks()  # Update "requested size" from geometry manager
        x = (window2.winfo_screenwidth() - window2.winfo_reqwidth()) / 2
        y = (window2.winfo_screenheight() - window2.winfo_reqheight()) / 2
        window2.geometry("+%d+%d" % (x-150, y-80))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        window2.deiconify()
        
        label = Label(window2, text=" Select From Option Menu: ",font=("Arial Bold Italic", 24),foreground= "dodgerblue3", bg = 'gray86')
        label.grid(column=0, row=0)

        def local():
           read_text()
            
            
        #Local file
        option1Button = Button(window2, text= "Parse Local File", bg="skyblue2", fg="black", command = local)
        option1Button.config(height = 1, width = 20)
        option1Button.grid(pady=15)

        def local2():
            read_from_web()
            
        #WEB
        option2Button = Button(window2, text= "Parse Website", bg="skyblue2", fg="black", command = local2)
        option2Button.config(height = 1, width = 20)
        option2Button.grid(pady=15)
            
        #ANALYTICS MENU
        option3Button = Button(window2, text= "Access Analytics Menu", bg="skyblue2", fg="black",command=  lambda: Stats_Menu_Gui(window2))
        option3Button.config(height = 1, width = 20)
        option3Button.grid(pady=15)

        def quite():
            window2.destroy()
            window.deiconify()
            
        goBackBtn = Button(window2, text="Go Back",bg="skyblue2", fg="black", command = quite)
        goBackBtn.grid(pady=15)

        
        window2.mainloop()
#******************************** END OF WINDOW 2 *************************

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

### ************************* WINDOW 3 *****************************************
def Stats_Menu_Gui(window2):
    window2.withdraw()

    #Initialize third frame (analytucs menu gui)
    window3 = Tk()
    window3.geometry("350x500")
    window3.title("ANALYTICS Menu")

    # Positioning the Window
    window3.update_idletasks()  # Update "requested size" from geometry manager
    x = (window3.winfo_screenwidth() - window3.winfo_reqwidth()) / 2
    y = (window3.winfo_screenheight() - window3.winfo_reqheight()) / 2
    window3.geometry("+%d+%d" % (x-100, y-150))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    window3.deiconify()

    #Freq
    label = Label(window3, text=" ANALYTICS MENU: ",font=("Times New Roman Bold Italic", 26),foreground= "dodgerblue3", bg='gray86')
    window3.configure(bg='gray86')
    label.grid(column=0, row=0)

    def local():
        sentece_word_tag()
    option5Button = Button(window3, text = 'Word Tagging', bg = 'skyblue2', fg = 'black', command = local)
    option5Button.config(height = 1, width = 20)
    option5Button.grid(pady = 15)

    def local2():
        stop_words()
        
    #Stop Words
    option2Button = Button(window3, text= "Stop Words", bg="skyblue2", fg="black", command = local2)
    option2Button.config(height = 1, width = 20)
    option2Button.grid(pady=15)

    def local3():
        stemming()
        
    option3Button = Button(window3, text = "Stemming", bg = "skyblue2", fg = "black", command = local3)
    option3Button.config(height = 1, width = 20)
    option3Button.grid(pady = 15)

    def local4():
        sentiment_analysis()
    option4Button = Button(window3, text = 'Sentiment Analysis', bg = 'skyblue2', fg = 'black', command = local4)
    option4Button.config(height = 1, width = 20)
    option4Button.grid(pady = 15)

    def local5():
        freq_Dist()
                      
    #LFrequency Distribution
    option1Button = Button(window3, text= "Frequency Distribution", bg="skyblue2", fg="black", command = local5)
    option1Button.config(height = 1, width = 20)
    option1Button.grid(pady=15)

    def local6():
        Synonym_analysis()
    option5Button = Button(window3, text = 'Synonym Analysis', bg = 'skyblue2', fg = 'black', command = local6)
    option5Button.config(height = 1, width = 20)
    option5Button.grid(pady = 15)
        
    def quite():
        window3.destroy()
        window2.deiconify()

    goBackBtn = Button(window3, text="Go Back",bg="skyblue2", fg="black", command = quite)
    goBackBtn.grid(pady=15)
    
    window3.mainloop()
#********************************* END OF WINDOW 3 **************************
