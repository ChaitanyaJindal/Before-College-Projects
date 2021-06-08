from tkinter import *

import tkinter.messagebox

import Data.BackEnd

class Student:

    def __init__(self,root):
        
        self.root = root
        self.root.title(" The Adhyyan School ")
        self.root.geometry("1326x670+15+0")
        self.root.configure(bg="light blue")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Addresst = StringVar()
        Mobile = StringVar()


        #===== Functions =======


        def stexit():
            stexit = tkinter.messagebox.askyesno(" The Adhyyan School ","Confirm if you want to exit")
            if stexit > 0:
                root.destroy()
                return


        def clearData():

            self.studentIDentry.delete(0,END)
            self.firstnameentry.delete(0, END)
            self.lastnameentry.delete(0,END)
            self.dateofBirthentry.delete(0,END)
            self.ageentry.delete(0,END)
            self.genderentry.delete(0,END)
            self.addressentry.delete(0,END)
            self.mobileentry.delete(0,END)


        def addData():

            if(len(StdID.get())!=0):
                Data.BackEnd.addstdrecord(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert((StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get()))


        def DisplayData():

            studentlist.delete(0,END)
            for row in Data.BackEnd.viewData():
                studentlist.insert(END,row,str(""))


        def StudentRec(event):

            global sd

            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.studentIDentry.delete(0,END)
            self.studentIDentry.insert(END,sd[0])

            self.firstnameentry.delete(0, END)
            self.firstnameentry.insert(END, sd[1])

            self.lastnameentry.delete(0,END)
            self.lastnameentry.insert(END, sd[2])

            self.dateofBirthentry.delete(0,END)
            self.dateofBirthentry.insert(END, sd[3])

            self.ageentry.delete(0,END)
            self.ageentry.insert(END, sd[4])

            self.genderentry.delete(0,END)
            self.genderentry.insert(END, sd[5])

            self.addressentry.delete(0,END)
            self.addressentry.insert(END, sd[6])

            self.mobileentry.delete(0,END)
            self.mobileentry.insert(END, sd[7])


        def DeleteData():

            if(len(StdID.get()) != 0):
                Data.BackEnd.deleterec(sd[0])
                clearData()
                DisplayData()


        def searchDatabase():

            studentlist.delete(0,END)

            for row in Data.BackEnd.searchData(StdID=StdID.get() ,Firstname= Firstname.get() ,Lastname=Lastname.get() ,Dob=Dob.get(), Age=Age.get() ,Gender=Gender.get() , Addresst=Addresst.get(),Mobile=Mobile.get()):
                studentlist.insert(END,row,str(""))


        def update():

            if (len(StdID.get())!=0):
                Data.BackEnd.deleterec(sd[0])

            if (len(StdID.get())!=0):
                Data.BackEnd.addstdrecord(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get() , Firstname.get() ,Lastname.get() ,Dob.get(), Age.get() ,Gender.get() , Addresst.get(),Mobile.get()))


        #======== Frames ========


        mainframe = Frame(self.root, width=1900,height=150, bd=10, relief= RIDGE,bg= "#F2F3F5")
        mainframe.grid(columnspan=2)


        bottomframe = Frame(self.root, width=1600, height=120, relief=GROOVE,bd=10,bg="#F2F3F5")
        bottomframe.grid(row=2, column=0, columnspan=2)


        rightframe = Frame(self.root,width=700,height=465, padx=8, pady=10, bd=14, relief=GROOVE, bg="#F2F3F5")
        rightframe.grid(row=1,column=1, sticky=W)


        leftframe =Frame(self.root, bd=15, height=900, relief=GROOVE, bg="#F2F3F5")
        leftframe.grid(row=1, column=0, sticky=E)


        #======== main FRame ============


        titlelabel = Label(mainframe, padx=90, text= "Student Database Management System", font= ('arial', 35, 'bold'),fg="green", bg="#F2F3F5")
        titlelabel.grid(row=0,column=0, sticky=W)


        #========== Left Frame ================


        photo = PhotoImage(file="Data/graduate.png")
        photoimage = photo.subsample(10, 10)

        a=Label( leftframe, bg="#F2F3F5",image= photoimage, text= "Student Info",font= ('arial', 30, 'bold'))
        a.image= photoimage
        a.grid(row=0, column=0, sticky=E)

        self.stdinfolable = Label(leftframe, pady=18, text= "Student Info",font= ('arial', 25, 'bold'))
        self.stdinfolable.grid(row=0,column=1, sticky=W)

        self.studentinfoframe = Frame(leftframe, width= 930, height=570, bg="#F2F3F5", relief=SUNKEN, bd=10)
        self.studentinfoframe.grid(row=1, column=0, columnspan=2, sticky=W)


        #======================================= student data entry =============================================


        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)

        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=0, column=0)

        self.studentIDlabel = Label(self.studentinfoframe, text="Student Id :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.studentIDlabel.grid(row=0, column=1)

        self.studentIDentry = Entry(self.studentinfoframe,textvariable=StdID, width=30, font=('arial', 15, 'bold'))
        self.studentIDentry.grid(row=0, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=1, column=0)

        self.firstnametlabel = Label(self.studentinfoframe, text= "First Name :",font= ('arial', 25, 'bold'),bg="#F2F3F5")
        self.firstnametlabel.grid(row=1, column=1)
      
        self.firstnameentry = Entry(self.studentinfoframe, width=30, textvariable=Firstname, font= ('arial', 15, 'bold'))
        self.firstnameentry.grid(row=1, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=2, column=0)

        self.lastnamelabel = Label(self.studentinfoframe, text="Last Name :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.lastnamelabel.grid(row=2, column=1)
      
        self.lastnameentry = Entry(self.studentinfoframe, width=30, textvariable=Lastname,font=('arial', 15, 'bold'))
        self.lastnameentry.grid(row=2, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=3, column=0)

        self.dateofBirthlabel = Label(self.studentinfoframe, text="Date of Birth :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.dateofBirthlabel.grid(row=3, column=1)
      
        self.dateofBirthentry = Entry(self.studentinfoframe, width=30,textvariable=Dob, font=('arial', 15, 'bold'))
        self.dateofBirthentry.grid(row=3, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=4, column=0)

        self.agelabel = Label(self.studentinfoframe, text="Age :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.agelabel.grid(row=4, column=1)
      
        self.ageentry = Entry(self.studentinfoframe, width=30,textvariable=Age, font=('arial', 15, 'bold'))
        self.ageentry.grid(row=4, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=5, column=0)

        self.genderlabel = Label(self.studentinfoframe, text="Gender :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.genderlabel.grid(row=5, column=1)
      
        self.genderentry = Entry(self.studentinfoframe, width=30, textvariable=Gender, font=('arial', 15, 'bold'))
        self.genderentry.grid(row=5, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=6, column=0)

        self.addresslabel = Label(self.studentinfoframe, text="Address :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.addresslabel.grid(row=6, column=1)
      
        self.addressentry = Entry(self.studentinfoframe, width=30, textvariable=Addresst, font=('arial', 15, 'bold'))
        self.addressentry.grid(row=6, column=2)

        photo2 = PhotoImage(file="Data/ha.png")
        photoimage2 = photo2.subsample(13, 13)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=7, column=0)

        self.mobilelabel = Label(self.studentinfoframe, text="Mobile :", font=('arial', 25, 'bold'), bg="#F2F3F5")
        self.mobilelabel.grid(row=7, column=1)
      
        self.mobileentry = Entry(self.studentinfoframe, width=30,textvariable=Mobile,font=('arial', 15, 'bold'))
        self.mobileentry.grid(row=7, column=2)

        photo2 = PhotoImage(file="Data/notes.png")
        photoimage2 = photo2.subsample(2, 2)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=0, column=4, rowspan=3, sticky=E+W)

        photo2 = PhotoImage(file="Data/Detail.png")
        photoimage2 = photo2.subsample(2, 2)
      
        a = Label(self.studentinfoframe, image=photoimage2)
        a.image = photoimage2
        a.grid(row=4, column=4, rowspan=4, sticky=E+W)
      
      
        #========== Right Frame ===========

        stddetailslable = Label(rightframe, text= "Student Details",font= ('arial', 30, 'bold'), pady=5)
        stddetailslable.grid(row=0, column=0, columnspan=2)

        xscrollbar = Scrollbar(rightframe, orient=HORIZONTAL)
        xscrollbar.grid(row=2, column=0, sticky=E+W)

        yscrollbar = Scrollbar(rightframe)
        yscrollbar.grid(row=1, column=1, sticky=N+S)

        studentlist = Listbox(rightframe,width=40,height=14,font=('arial',16,'bold'), xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        studentlist.bind("<<ListboxSelect>>",StudentRec)
        studentlist.grid(row=1, column=0)

        xscrollbar.config(command = studentlist.xview)
        yscrollbar.config(command = studentlist.yview)

        photo2 = PhotoImage(file="Data/details.png")
        photoimage2 = photo2.subsample(4,5)

        a = Label(rightframe, image=photoimage2)
        a.image = photoimage2
        a.place(x=40, y=0)


        #========= Button Sections ==========


        addnewbutton = Button(bottomframe, command= addData, text="Add New", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        addnewbutton.grid(row=0, column=0)

        displaybutton = Button(bottomframe, command= DisplayData, text="Display", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        displaybutton.grid(row=0, column=1)

        clearbutton = Button(bottomframe, command=clearData, text="Clear", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        clearbutton.grid(row=0, column=2)

        deletebutton = Button(bottomframe, command=DeleteData, text="Delete", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        deletebutton.grid(row=0, column=3)

        searchbutton = Button(bottomframe, command=searchDatabase, text="Search ", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        searchbutton.grid(row=0, column=4)

        updatebutton = Button(bottomframe, command=update, text="Update", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        updatebutton.grid(row=0, column=5)

        exitbutton = Button(bottomframe, command=stexit, text="Exit", fg="white", bg="#8D2752", font=('arial', 18, 'bold'), relief=SUNKEN, bd=5, height=2, width=11)
        exitbutton.grid(row=0, column=6)


if __name__== '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
