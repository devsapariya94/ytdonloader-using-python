import win32gui, win32con
hide=win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

from pytube import YouTube 
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from threading import *
import config
from tkinter import messagebox
root=Tk()
photo = PhotoImage(file = "ytdownloader.png")
root.iconphoto(False, photo)
root.title('youtube downloader')
root.geometry('700x350')

root.resizable(width=False, height=False)
#root.protocol ('WM_DELETE_WINDOW', (lambda: 'pass') ())
global var
global link
global var2
global info
var=StringVar()
var2=StringVar()
head=Label(root, text="YOUTUBE DOWNLOADER", font=('Helvetica',30), bg='black', fg='white')
head.grid(row=1, column=2, columnspan=2)
linkl=Label(root, text="Past Link", bg='black', fg='white')
linkl.grid(row=3, column=1)
linkl.config(width=10, font=('Helvetica',15), bg='black', fg='white')

linke= Entry(root, width=60, font='large_font',borderwidt=2)
linke.grid(row=3, column=2,columnspan=1,pady=5)

testl=Label(root, text='Video Quality', font=('Helvetica',15),bg='black', fg='white')
testl.grid(row=2, column=1)

testlist = [
"720 P",
"480 P",
"360 P",
"240 P",
"144 P"
 ]

variable = StringVar()
variable.set(testlist[0])
test= OptionMenu(root ,variable, *testlist)
test.config(width=10, font=('Helvetica',8), bg='black', fg='white')
test.grid(row=2, column=2)


head=Label(root, textvariable=var, font=('Helvetica',25), bg='black', fg='white')
head.grid(row=4, column=1, columnspan=2)
var.set('')
head2=Label(root, textvariable=var2, font=('Helvetica',25), bg='black', fg='white')
head2.grid(row=5, column=1, columnspan=2)
var2.set('')
head3=Label(root, text='Created by Dev Sapariya', font=('Helvetica',10), bg='black', fg='white')
head3.grid(row=8, column=1, columnspan=2)

def complete (stream=None , file_path=None):
        showinfo("message", "Download Compeleted.......")
        var.set('')
        root.update()
        linke.delete(0,END)
        var2.set('')
        root.update()
        btn['text']='SELECT FOLDER TO DOWNLOAD'
        btn['state']='active'

def progress(streamsNone ,chunk=None, bytes_remaining=None):
        size_t=int(config.size)
        per=((size_t-bytes_remaining)/size_t)*100
        btn['text']="{:00.00f}% downloaded".format(per)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
def down(link):
        
        try:
            var2.set('')
            root.update()
            global yt
            yt = YouTube(link)
            
            titel=yt.title[:40]+'...'
            var2.set(titel)
            
            root.update()
        
        except:
                var.set('')
                root.update()
                linke.delete(0,END)
                btn['text']='TRY AGAIN'
                btn['state']='active'
                

                var2.set("Connection Error OR link is worng")
                root.update()
        quality=str(variable.get())
        
        if quality=='720 P':
        
                try:
                    d_video = yt.streams.get_by_itag(22)
                
                    config.size=(str(d_video.filesize))
                                      
                    yt.register_on_complete_callback(complete)
                    yt.register_on_progress_callback(progress)
                    d_video.download(SAVE_PATH)
                    
                except:
                            
                            var.set('')
                            root.update()
                            linke.delete(0,END)
                            btn['text']='TRY AGAIN'
                            btn['state']='active'
                            print(e)
                            var2.set('SOME ERROR!,Try with diff. quaility')
                            root.update()
                            

        elif quality=='480 P':
                try:
                    d_video = yt.streams.get_by_itag(135)
                    config.size=(str(d_video.filesize))
                                      
                    yt.register_on_complete_callback(complete)
                    yt.register_on_progress_callback(progress)
                    d_video.download(SAVE_PATH)
           
                except:
                    
                            var.set('')
                            root.update()
                            linke.delete(0,END)
                            btn['text']='TRY AGAIN'
                            btn['state']='active'

                            var2.set('SOME ERROR!,Try with diff. quaility')
                            root.update()
        elif quality=='360 P':
                try:
                    
                    d_video = yt.streams.get_by_itag(134)
                    
                    config.size=(str(d_video.filesize))
                    
                    yt.register_on_complete_callback(complete)
                    yt.register_on_progress_callback(progress)
                    d_video.download(SAVE_PATH)
                               
                except:
                            
                            var.set('')
                            
                            root.update()
                            
                            linke.delete(0,END)
                           
                            btn['text']='TRY AGAIN'
                            btn['state']='active'
                                
                            var2.set('SOME ERROR!,Try with diff. quaility')
                            root.update()



        elif quality=='240 P':
                try:
                    d_video = yt.streams.get_by_itag(133)
                    config.size=(str(d_video.filesize))
                    
                    yt.register_on_complete_callback(complete)
                    yt.register_on_progress_callback(progress)
                    d_video.download(SAVE_PATH)

                   
                except:
                        var.set('')
                        root.update()
                        linke.delete(0,END)
                        btn['text']='TRY AGAIN'
                        btn['state']='active'
        
                        var2.set('SOME ERROR!,Try with diff. quaility')
                        root.update()

        elif quality=='144 P':
                try:
                    d_video = yt.streams.get_by_itag(160)
                    config.size=(str(d_video.filesize))
                    yt.register_on_complete_callback(complete)
                    yt.register_on_progress_callback(progress)
                    d_video.download(SAVE_PATH)

                   
                except:
                        var.set('')
                        root.update()
                        linke.delete(0,END)
                        btn['text']='TRY AGAIN'
                        btn['state']='active'

                        var2.set('SOME ERROR!,Try with diff. quaility')
                        root.update()    
                 
def clik():
    root.filename =  filedialog.askdirectory()
    global SAVE_PATH
    save= root.filename
    s=''
    for i in save:
        if i=='/':
                    s=s+i+'/'
        else:
                     s=s+i
    SAVE_PATH=s
    if(SAVE_PATH==''):
        pass
    else:
        loc='file save @ ' +SAVE_PATH
        var.set(loc)
        root.update()
        link=linke.get()
        if link=='':
            var2.set("enter link")
            root.update()
        else:
            btn['text']='Please Wait..'
            btn['state']='disabled'
            
            thread=Thread(target=down , args=(link,))
            thread.start()

    

        
        


        
btn=Button(root, text='SELECT FOLDER TO DOWNLOAD' , command=clik, width=25, height=2, bg='black', fg='white',relief='ridge' ,borderwidth=5)
btn.grid(row=6, column=1, columnspan=2)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.config(bg='black')
root.mainloop()
