"""
    Written By Marcus Whelan for Senior 1 project 2
    This is the Main Graphical User Interface
    the user will do everything from this end.
    all editing and sending of data is done here.
"""

LARGE_FONT=("Verdana", 18)

import Tkinter as tk
from Tkinter import *
import XL
import RDC
import signal
from easyprocess import EasyProcess
import sys
import logging
import datetime


from tkMessageBox import *

class The_Gui(tk.Tk):
    #Main Setup for all Pages
    # NEED THIS TO RUN
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.geometry("478x283")
        tk.Tk.wm_title(self,"Double A&M Productions")

        #needed to build the frame that all windows display in
        container = tk.Frame(self)
        """ needed for expandable use but really could not
        be used if really didnt need it. but I feel it is usefull
        """
        container.pack(side = "top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)

        """------needed for pages to work together-------"""
        self.frames={}

        # for loop to loop through frames
        for F in (StartPage,Login,StartStop,EditPage,Number_Pad,
                  ChangeTime,ChangeCName,SelectClass,ScanStudent,
                  EditClasses,EditStudents,Keyboard,ChangeTardy):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    


"""------------------START Making Pages---------------------"""
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg="orange red")
        v = StringVar()
        v.set(XL.getClass())
        label=tk.Label(self,textvariable=v,font=LARGE_FONT,bg="orange red")
        label.grid(row=1,column=1,sticky=N,padx=20,pady=20)
        #space label for formatting
        space_label = tk.Label(self,text="   ",bg="orange red")
        space_label.grid(row=2,column=0,padx=50)

        button1=tk.Button(self, text="Login",height=4,width=12,padx=4,pady=4,bd=4,
                          command = lambda: controller.show_frame(Login))
        button1.grid(row=2,column=1,padx=50)
        #refresh label
        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=3,column=1,pady=20)
        def Refresh():
            v.set(XL.getClass())
            label.configure(text=v)

"""-----------------------LOGIN PAGE-----------------------"""
class Login(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Login",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column =2, sticky = N)
        #entry field
        v = StringVar()
        inputbox = Entry(self,textvariable = v)
        inputbox.grid(row=1,column=2)
        """
        -----------------------------------------------
        Methods for making the buttons enter into the
        text field and be able to have the password
        let you go to the next page or not
        -----------------------------------------------
        """
        def input_number(number):
            inputbox.insert(END,number)
        def go_back():
            inputbox.delete(0,END)
            controller.show_frame(StartPage)
        def submit():
            if(int(inputbox.get()) == int(XL.getP())):
                inputbox.delete(0,END)
                controller.show_frame(StartStop)
            else:
                inputbox.delete(0,END)
                showerror(title="Error",message="Access Denied")
        """------------------------------------------------------
        Padding for the Buttons
        """
        self.columnconfigure(1,pad=15)
        self.columnconfigure(2,pad=3)
        self.columnconfigure(3,pad=15)
        self.rowconfigure(3,pad=30)
        self.rowconfigure(4,pad=3)
        self.rowconfigure(5,pad=30)
        #button 7
        button7 = tk.Button(self,text="7",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("7"),height=2,width=5)
        button7.grid(row=3,column=1)
        #button 8
        button8 = tk.Button(self,text="8",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("8"),height=2,width=5)
        button8.grid(row=3,column=2)
        #button 9
        button9 = tk.Button(self,text="9",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("9"),height=2,width=5)
        button9.grid(row=3,column=3)
        #button 4
        button4 = tk.Button(self,text="4",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("4"),height=2,width=5)
        button4.grid(row=4,column=1)
        #button 5
        button5 = tk.Button(self,text="5",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("5"),height=2,width=5)
        button5.grid(row=4,column=2)
        #button 6
        button6 = tk.Button(self,text="6",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("6"),height=2,width=5)
        button6.grid(row=4,column=3)
        #button 1
        button1 = tk.Button(self,text="1",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("1"),height=2,width=5)
        button1.grid(row=5,column=1)
        #button 2
        button2 = tk.Button(self,text="2",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("2"),height=2,width=5)
        button2.grid(row=5,column=2)
        #button 3
        button3 = tk.Button(self,text="3",bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                    command = lambda: input_number("3"),height=2,width=5)
        button3.grid(row=5,column=3)
        #Submit
        Submit = tk.Button(self,text="Submit",
                    command = lambda: submit(),height=2,width=4)
        #Submit.grid(row=5,column=4)
        Submit.place(x=410,y=240)
        #back
        Back = tk.Button(self,text="<<Back",
                    command = lambda: go_back())
        Back.grid(row=0,column=0)
"""------------------START STOP PAGE----------------------------"""
class StartStop(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        hasstarted = StringVar()
        hasstarted.set(" ")

        """
        =====================================================================
        Most important function in program. will go line by line on this
        1>> This sets the class start to on so the loop will start and not break
        2-3>Buzz 2 times signals start of class
        4>> this line sets the class start time to that specific lecture sheet
        5>> gets EndOfClass time .. adds start time and class time together
        6>> makes a zero in datetime reference 00:00:00 to use later
        7>> this checks if while(Time left in class > 00:00:00)
        8>> If statement check inside loop if the class is still on
        9>> read in the RFID or wait 5 seconds to loop again
        10> if there is a card read in
        11> format big string into rfid number
        12> places students RFID number and if tardy into the lecture day
        13> 
        14> Buz once to let the user know the card was read in
        15> else the class is no longer on
        16> Set increment day to False so as to let user know the inc
            has not occured yet
        17-19> buz 3 times to let user know class was cancelled
        20> break out of while loop
        21> increment the day of class
        22> set inc to true to let program know the day was incremented
        =====================================================================
        """
        def Start_Class(boo):
            RDC.setison(boo)
            RDC.buz()
            RDC.buz()
            currentT = RDC.getCT()
            XL.setClassS()
            EOC = RDC.getEOC()
            zero = RDC.setT(0,0)
            while((EOC-RDC.getCT())>zero):
                print "time out"
                if(RDC.getison()):
                    print "3"
                    ext = EasyProcess('/home/pi/libnfc/libnfc-1.7.1/examples/nfc-poll').call(timeout=5).stdout
                    print " 4"
                    if(ext):
                        temp = RDC.formatC(ext)
                        if(temp == "d198290f"):
                            break;
                        XL.placeStudent(temp,currentT)
                        #take photo and record him/her
                        RDC.buz()
                        print("student added")
                else:
                    RDC.setinc(False)   
                    break;
            RDC.buz()
            RDC.buz()
            RDC.buz()
            XL.incLectDay()
            day = XL.getLectDay()
            lecture = XL.getLD()
            if(day > lecture):
                showerror(title="Error",message="That was the last day of class.")
            RDC.setinc(True)
        def Upload():
            XL.emailCXL()
            RDC.buz2()
            RDC.buz2()
            RDC.buz2()
            RDC.buz2()
        def Refresh():
            v.set(XL.getClass())
            label3.configure(text=v)
        #start Label
        label2 = tk.Label(self,text="",font=LARGE_FONT,bg="orange red")
        label2.grid(row=0,column=1,padx=100)
        #Start button
        Start= tk.Button(self,text="Start",height=4,width=8,relief="raised",
                         padx=4,pady=4,bd=4,command = lambda: Start_Class(True))
        Start.grid(row=1,column=1)
        v = StringVar()
        v.set(XL.getClass())
        #stop label
        label3 = tk.Label(self,textvariable=v,font=LARGE_FONT,bg="orange red")
        label3.grid(row=2,column=1,padx=100)

        #upload button
        upload= tk.Button(self,text="Upload",height=4,width=8,relief="raised",
                        padx=4,pady=4,bd=4, command = lambda: Upload())
        upload.grid(row=3,column=1)
        
        #edit button
        edit = tk.Button(self,text="Edit",height=4,width=6,
                             relief="raised",padx=4,pady=4,bd=4,
                             command = lambda: controller.show_frame(EditPage))
        edit.grid(row=3,column=2)
        #refresh button
        refresh=tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=3,column=0)

        #back button
        Back=tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda:controller.show_frame(Login))
        Back.grid(row=0,column=0)

""""-----------------------EDIT PAGE------------------------------"""
class EditPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Edit",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1)
        #change class time length button
        changeT=tk.Button(self,text="Change class Time",relief="raised",padx=4,
                height=2,pady=4,bd=4,
                    command=lambda:controller.show_frame(ChangeTime))
        changeT.grid(row=1,column=1,pady=15,padx=20)
        #change class name button
        changeN=tk.Button(self,text="Change class name",relief="raised",padx=4,
                height=2,pady=4,bd=4,
                        command=lambda:controller.show_frame(ChangeCName))
        changeN.grid(row=2,column=1,pady=10,padx=20)
        #select class button
        selectC=tk.Button(self,text="Select class",relief="raised",padx=4,
                height=2,pady=4,bd=4,
                        command=lambda:controller.show_frame(SelectClass))
        selectC.grid(row=3,column=1,pady=5,padx=20)
        #edit tardy time
        tardy=tk.Button(self,text="Edit Tardy time",relief="raised",padx=4,
                height=2,pady=4,bd=4,
                        command=lambda:controller.show_frame(ChangeTardy))
        tardy.grid(row=1,column=2,pady=15,padx=10)
        #edit Classes
        editClass=tk.Button(self,text="Edit Classes",relief="raised",padx=4,pady=4,
                height=2,bd=4,command=lambda:controller.show_frame(EditClasses))
        editClass.grid(row=3,column=2,pady=10,padx=5)
        #edit students
        editstudents=tk.Button(self,text="Edit Students",relief="raised",padx=4,
                height=2,pady=4,bd=4,
                        command=lambda:controller.show_frame(EditStudents))
        editstudents.grid(row=2,column=2,pady=10,padx=20)
        def ChangeLectDay():
            XL.setLastPage("EditPageL")
            controller.show_frame(Number_Pad)
        #lecture button
        LD=tk.Button(self,text="Lecture Day",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,
                        command = lambda: ChangeLectDay())
        LD.grid(row=1,column=0,pady =15)
        def ChangeP():
            XL.setLastPage("EditPage")
            controller.show_frame(Number_Pad)
        #password button
        password = tk.Button(self,text="Password",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,
                        command = lambda: ChangeP())
        password.grid(row=2,column=0)
        def ChangeEmail():
            XL.setLastPage("EditPage")
            controller.show_frame(Keyboard)
        #email button
        mail=tk.Button(self,text="Email",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,
                        command = lambda: ChangeEmail())
        mail.grid(row=3,column=0)
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,
                        command = lambda: controller.show_frame(StartStop))
        Back.grid(row=0,column=0)
"""-------------------Change class time length----------------------------"""      
class ChangeTime(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Change Class",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1,sticky=N)
        label3=tk.Label(self,text="Time Length",font=LARGE_FONT,bg="orange red")
        label3.grid(row=1,column=1,sticky=N)
        #get class hour time
        hours = StringVar()
        hours.set(XL.getH())
        #get class minute time
        minutes = StringVar()
        minutes.set(XL.getM())
        #refresh buttons
        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=4,column=3)
        def Refresh():
            hours.set(XL.getH())
            hoursB.configure(text=hours)
            minutes.set(XL.getM())
            minutesB.configure(text=minutes)
        #change hours button
        hoursB=tk.Button(self,textvariable=hours,bg="orange red",
                         height=4,width=15,command=lambda: go_NPadH())
        hoursB.grid(row=2,column=1,pady=10)
        def go_NPadH():
            XL.setLastPage("ChangeTimeH")
            controller.show_frame(Number_Pad)
        #Hours label
        label4=tk.Label(self,text="Hours",font=LARGE_FONT,bg="orange red")
        label4.grid(row=3,column=1,sticky=N)
        # label :
        label2=tk.Label(self,text=":",font=LARGE_FONT,bg="orange red")
        label2.grid(row=2,column=2) 
        #change minutes button
        minutesB=tk.Button(self,textvariable=minutes,bg="orange red",
                           height=4,width=15,command=lambda: go_NPadM())
        minutesB.grid(row=2,column=3,pady=10)
        def go_NPadM():
            XL.setLastPage("ChangeTimeM")
            controller.show_frame(Number_Pad)
        #minutes label
        label5=tk.Label(self,text="Minutes",font=LARGE_FONT,bg="orange red")
        label5.grid(row=3,column=3,sticky=N)
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("ChangeTime")
            controller.show_frame(EditPage)
"""-------------------ChangeCName----------------------------"""      
class ChangeCName(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        #refresh label
        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=0,column=2)
        def Refresh():
            clas.set(XL.getClass())
            label2.configure(text=clas)
        #line1
        v = StringVar()
        label=tk.Label(self,textvariable=v,font=LARGE_FONT,bg="orange red")
        label.grid(row=1,column=2,sticky=N)
        v.set("This will change the name")
        #line2
        v2 = StringVar()
        label3=tk.Label(self,textvariable=v2,font=LARGE_FONT,bg="orange red")
        label3.grid(row=2,column=2)
        v2.set("of the current class you are in")
        #where To put the class that is alctually being held 
        clas=StringVar()
        clas.set(XL.getClass())
        label2=tk.Label(self,textvariable=clas,font=LARGE_FONT,bg="orange red")
        label2.grid(row=3,column=2)
        #change class name button
        change=tk.Button(self,text="Rename Class",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=15,command=lambda: go_Keyboard())
        change.grid(row=4,column=2)
        def go_Keyboard():
            XL.setLastPage("ChangeCName")
            controller.show_frame(Keyboard)
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("ChangeCname")
            controller.show_frame(EditPage)
"""-------------------Select Class----------------------------"""      
class SelectClass(tk.Frame):
    def __init__(self,parent,controller):
        array = []
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Select Class",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1,padx=20,sticky=N)

        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=3,column=0)
        def Refresh():
            array = XL.getClasses()
            listbox.delete(0,END)
            for item in array:
                listbox.insert(END,item)
                listbox.insert(END," ")
        
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=3,column=2,sticky=N+S)
        listbox = Listbox(self,yscrollcommand=scrollbar.set,height=10)
        listbox.grid(row=3,column=1,pady = 20)
        scrollbar.config(command=listbox.yview)
        array = XL.getClasses()
        for item in array:
            listbox.insert(END,item)
            listbox.insert(END," ")
        #Select Button
        select=tk.Button(self,text="Select",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Selected())
        select.grid(row=3,column=3,padx= 20)
        def Selected():
            selection = listbox.selection_get()
            XL.setClass(selection)
        #back button
        Back=tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("ChangeCname")
            controller.show_frame(EditPage)
"""---------------Change Tardy time for class-------------------"""
class ChangeTardy(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Change Class",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1,sticky=N)
        label3=tk.Label(self,text="Late Time",font=LARGE_FONT,bg="orange red")
        label3.grid(row=1,column=1,sticky=N)
        #get class tardy time
        Ttime = StringVar()
        Ttime.set(XL.getTTime())
        
        #refresh buttons
        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=4,column=3)
        def Refresh():
            Ttime.set(XL.getTTime())
            tardy.configure(text=Ttime)
        #change hours button
        tardy=tk.Button(self,textvariable=Ttime,bg="orange red",
                         height=4,width=15,command=lambda: change())
        tardy.grid(row=2,column=1,pady=10)
        def change():
            XL.setLastPage("ChangeTardy")
            controller.show_frame(Number_Pad)
        #late label
        label4=tk.Label(self,text="Late after",font=LARGE_FONT,bg="orange red")
        label4.grid(row=3,column=1,sticky=N)
        #late label
        label3=tk.Label(self,text="this many minutes",font=LARGE_FONT,bg="orange red")
        label3.grid(row=4,column=1,sticky=N)
       
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("ChangeTime")
            controller.show_frame(EditPage)
"""-------------------edit Studetents----------------------------"""
class EditStudents(tk.Frame):
    def __init__(self,parent,controller):
        array = []
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Edit",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1,padx=20,sticky=N)

        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=3,column=0)
        def Refresh():
            array = XL.getStudents()
            listbox.delete(0,END)
            for item in array:
                listbox.insert(END,item)
                listbox.insert(END," ")
        
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=3,column=2,sticky=N+S,padx=50)
        listbox = Listbox(self,yscrollcommand=scrollbar.set,height=10)
        listbox.grid(row=3,column=1,pady = 20)
        scrollbar.config(command=listbox.yview)
        array = XL.getStudents()
        for item in array:
            listbox.insert(END,item)
            listbox.insert(END," ")
        #Delete Button
        delete=tk.Button(self,text="Remove",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Delete())
        delete.grid(row=3,column=3)
        def Delete():
            selection = listbox.selection_get()
            XL.delStudent(selection)
            Refresh()
        #add button
        add=tk.Button(self,text="Add Student",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Add())
        add.grid(row=0,column=3)
        def Add():
            XL.setLastPage("EditStudents")
            controller.show_frame(Keyboard)
        #back button
        Back=tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("EditStudents")
            controller.show_frame(EditPage)
"""-------------------Edic Classes----------------------------"""      
class EditClasses(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="Edit",font=LARGE_FONT,bg="orange red")
        label.grid(row=0,column=1,sticky=N)

        refresh= tk.Button(self,text="Refresh",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Refresh())
        refresh.grid(row=3,column=0)
        def Refresh():
            array = XL.getClasses()
            listbox.delete(0,END)
            for item in array:
                listbox.insert(END,item)
                listbox.insert(END," ")
        
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=3,column=2,sticky=N+S,padx=50)
        listbox = Listbox(self,yscrollcommand=scrollbar.set,height=10)
        listbox.grid(row=3,column=1,pady = 20)
        scrollbar.config(command=listbox.yview)
        array = XL.getClasses()
        for item in array:
            listbox.insert(END,item)
            listbox.insert(END," ")
        #Delete Button
        delete=tk.Button(self,text="Remove",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Delete())
        delete.grid(row=3,column=3)
        def Delete():
            selection = listbox.selection_get()
            XL.delClass(selection)
            Refresh()
        #add button
        add=tk.Button(self,text="Add Class",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: Add())
        add.grid(row=0,column=3)
        def Add():
            XL.setLastPage("EditClasses")
            controller.show_frame(Keyboard)
        #back button
        Back=tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("EditClasses")
            controller.show_frame(EditPage)
"""----------------Scan Student------------------------------"""
class ScanStudent(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        #back button
        Back = tk.Button(self,text="<<Back",relief="raised",padx=4,pady=4,bd=4,
                height=2,width=10,command = lambda: go_Page())
        Back.grid(row=0,column=0)
        def go_Page():
            XL.setLastPage("Scan Student")
            controller.show_frame(EditStudents)
        
        label=tk.Label(self,text="SCAN",font=LARGE_FONT,bg="orange red")
        label.grid(row=1,column=1,sticky=N)
        #scan button
        scan=tk.Button(self,text="Scan Student in",relief="raised",padx=4,
                       pady=4,bd=4,height=4,command= lambda: scan_in())
        scan.grid(row=2,column=1,pady=40,padx = 100)
        def scan_in():
            UID=EasyProcess('/home/pi/libnfc/libnfc-1.7.1/examples/nfc-poll').call(timeout=10).stdout
            if(UID):
                UID = RDC.formatC(UID)
                lname = XL.getLstudent()
                XL.addStudent(lname)
                XL.addUID(UID)
                RDC.buz()
                controller.show_frame(EditStudents)
            else:
                showerror(title="Error",message="No Card was recorded.")
                print "time out"
                
"""
-----------------------------------------------------------------------------------
===================================================================================
                    Number pads for time entering
===================================================================================
-----------------------------------------------------------------------------------
"""
###############################################
#           Entering in Hours                 #
###############################################
class Number_Pad(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        inputbox = Entry(self)
        inputbox.grid(row=1,column=1,columnspan=3,padx=57)
        def input_number(number):
            inputbox.insert(END,number)
        def Save():
            if(XL.getPage() == "ChangeTimeM"):
                XL.setLastPage("Number_Pad")
                new_MT = inputbox.get()
                XL.changeM(new_MT)
                inputbox.delete(0,END)
                controller.show_frame(ChangeTime)
            elif(XL.getPage() == "ChangeTimeH"):
                XL.setLastPage("Number_Pad")
                new_HT = inputbox.get()
                XL.changeH(new_HT)
                inputbox.delete(0,END)
                controller.show_frame(ChangeTime)
            elif(XL.getPage() == "EditClasses"):
                cname = XL.getLclass()
                lectures = inputbox.get()
                XL.createClass(cname,lectures)
                inputbox.delete(0,END)
                controller.show_frame(EditClasses)
            elif(XL.getPage() == "ChangeTardy"):
                newTTime = inputbox.get()
                XL.setTTime(newTTime)
                inputbox.delete(0,END)
                controller.show_frame(ChangeTardy)
            elif(XL.getPage() == "EditPage"):
                newP = inputbox.get()
                XL.setP(newP)
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
            elif(XL.getPage() == "EditPageL"):
                lecture = inputbox.get()
                XL.setLectDay(int(lecture))
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
        def back():
            if(XL.getPage() == "ChangeTimeH"):
                XL.setLastPage("Number_Pad")
                inputbox.delete(0,END)
                controller.show_frame(ChangeTime)
            elif(XL.getPage() == "ChangeTimeM"):
                XL.setLastPage("Number_Pad")
                inputbox.delete(0,END)
                controller.show_frame(ChangeTime)
            elif(XL.getPage() == "EditClasses"):
                inputbox.delete(0,END)
                controller.show_frame(EditClasses)
            elif(XL.getPage() == "ChangeTardy"):
                inputbox.delete(0,END)
                controller.show_frame(ChangeTardy)
            elif(XL.getPage() == "EditPage"):
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
            elif(XL.getPage() == "EditPageL"):
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
        def delete():
            inputbox.delete(0,END)
        """
        This is made to make the entire keyboard so it will fit
        inside the small touch screen. except for
        Back, and submit
        """
        buttons=['7','8','9',
                 '4','5','6',
                 '1','2','3',
                     '0','del']
        rowv = 2
        colv = 1
        for b in buttons:
            command = lambda x=b: input_number(x)
            if b != "del":
                tk.Button(self,text=b,width=3,height=2,bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                      command=command).grid(row=rowv,column=colv,
                                            padx=10,pady=5)
            else:
                tk.Button(self,text=b,width=3,height=2,bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                      command= lambda: delete()).grid(row=rowv,column=colv)  
            colv +=1
            if colv>3 and rowv == 2:
                colv=1
                rowv+=1
            if colv>3 and rowv == 3:
                colv=1
                rowv+=1
            if colv>3 and rowv == 4:
                colv=1
                rowv+=1
            if colv>3 and rowv == 5:
                colv=1
                rowv+=1
        #back button
        Back = tk.Button(self,text="Back",width=10,height=2,pady=4,padx=4,
                    bd=3,command = lambda: back())
        Back.grid(row=0,column=0)
        #save
        save=tk.Button(self,text="Save",width=10,height=2,pady=4,padx=4,
                    bd=3,command = lambda: Save())
        save.grid(row=0,column=4)
######################################################
#           Keyboard for changing class name         #
######################################################
class Keyboard(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg = "orange red")
        label=tk.Label(self,text="",bg="orange red")
        label.grid(row=0,column =4,sticky=N)
        inputbox = Entry(self)
        inputbox.grid(row=1,columnspan=12)
        def input_letter(letter):
            inputbox.insert(END,letter)
        def save():
            if(XL.getPage() == "ChangeCName"):
                XL.setLastPage("Keyboard")
                new_name = inputbox.get()
                XL.changeCName(new_name,XL.getClass())
                inputbox.delete(0,END)
                controller.show_frame(ChangeCName)
            elif(XL.getPage() == "EditStudents"):
                XL.setLastPage("Keyboard")
                XL.setLstudent(inputbox.get())
                inputbox.delete(0,END)
                controller.show_frame(ScanStudent)
            elif(XL.getPage() == "EditClasses"):
                XL.setLclass(inputbox.get())
                inputbox.delete(0,END)
                controller.show_frame(Number_Pad)
            elif(XL.getPage() == "EditPage"):
                XL.setEmail(inputbox.get())
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
        def back():
            if(XL.getPage() == "ChangeCName"):
                XL.setLastPage("Keyboard")
                inputbox.delete(0,END)
                controller.show_frame(ChangeCName)
            elif(XL.getPage() == "EditStudents"):
                XL.setLastPage("Keyboard")
                inputbox.delete(0,END)
                controller.show_frame(EditStudents)
            elif(XL.getPage() == "EditClasses"):
                XL.setLastPage("Keyboard")
                inputbox.delete(0,END)
                controller.show_frame(EditClasses)
            elif(XL.getPage() == "EditPage"):
                inputbox.delete(0,END)
                controller.show_frame(EditPage)
        def delete():
            inputbox.delete(0,END)
        """
        This is made to make the entire keyboard so it will fit
        inside the small touch screen. except for
        Space, Back, and submit
        """
        buttons=['1','2','3','4','5','6','7','8','9','0',
                 'Q','W','E','R','T','Y','U','I','O','P',
                 'A','S','D','F','G','H','J','K','L','-',
                 'Z','X','C','V','B','N','M','_','.','del']
        rowv = 2
        colv = 0
        for b in buttons:
            command = lambda x=b: input_letter(x)
            if b != "del":
                tk.Button(self,text=b,width=3,height=2,bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                      command=command).grid(row=rowv,column=colv)
            else:
                tk.Button(self,text=b,width=3,height=2,bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                      command= lambda: delete()).grid(row=rowv,column=colv)   
            colv +=1
            if colv>9 and rowv == 2:
                colv=0
                rowv+=1
            if colv>9 and rowv == 3:
                colv=0
                rowv+=1
            if colv>9 and rowv == 4:
                colv=0
                rowv+=1
            if colv>9 and rowv == 5:
                colv=0
                rowv+=1 
        #back button
        Back = tk.Button(self,text="Back",width=6,height=1,pady=4,padx=4,
                    bd=3,command = lambda: back())
        Back.grid(row=0,column=0)
        #save
        save_new=tk.Button(self,text="Save",width=6,height=1,pady=4,padx=4,
                    bd=3,command = lambda: save())
        save_new.grid(row=0,column=9)
        #space
        space=tk.Button(self,text="Space",width=40,bg="#000000",fg="#ffffff",
                    activebackground="#ffffff",activeforeground="#000000",
                    relief="raised",padx=4,pady=4,bd=4,height=2,
                    command=lambda: input_letter(" "))
        space.grid(row=6,columnspan=16)
        # @ button
        att=tk.Button(self,text="@",width=3,height=2,bg="#000000",fg="#ffffff",
                      activebackground="#ffffff",activeforeground="#000000",
                      relief='raised',padx=4,pady=4,bd=3,
                      command=lambda: input_letter("@")).grid(row=6,column=0)
        
app = The_Gui()
app.mainloop()





















        
