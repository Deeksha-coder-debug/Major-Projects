from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import mysql.connector as my
from tkinter import messagebox
# import db

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        # Set the background color of the entire interface
        self.root.configure(bg="lightblue")  # You can use any color name or hex code

        self.nameoftablets=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.nooftablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.furtherinfo=StringVar()
        self.bloodpressure=StringVar()
        self.storage=StringVar()
        self.howtousemedication=StringVar()
        self.patientid=StringVar()
        self.patientname=StringVar()
        self.dateofbirth=StringVar()
        self.patientaddress=StringVar()
        self.doctorname=StringVar()

        #label creation
        #bd is border width
        label=Label(self.root,text='HOSPITAL MANAGEMENT SYSTEM',bd=20,relief='ridge',fg='red',bg='white',font=('times new roman',50,'bold'))
        label.pack(side=TOP,fill='x')

        #upper dataframe creation
        # A Frame is a simple container widget that can hold other widgets. 
        # It is primarily used for organizing the layout of your application

        Dataframe=Frame(self.root,bd=20,relief='ridge')
        Dataframe.place(x=0,y=130,width=1530,height=400)

        #creating 2 sub frames inside the upper parent frame

        # A LabelFrame is a specialized type of Frame that 
        # includes a label (title) at the top. It is used to group related
        # widgets together and provide a title for that group.

        # padx: This option adds horizontal padding (space) on the left and 
        # right sides of the widget. It can be specified in pixels.
        # pady: This option adds vertical padding (space) on the top
        #  and bottom sides of the widget. It can also be specified in pixels.

        leftframe=LabelFrame(Dataframe,bd=10,relief='ridge',padx=20,font=('arial',12,'bold'),text='Patient Information')
        leftframe.place(x=0,y=5,width=980,height=350)

        rightframe=LabelFrame(Dataframe,bd=10,relief='ridge',padx=20,font=('arial',12,'bold'),text='Prescription')
        rightframe.place(x=990,y=5,width=460,height=350)

        #lower frame for buttons
        Buttonframe=Frame(self.root,bd=20,relief='ridge')
        Buttonframe.place(x=0,y=530,width=1530,height=100)
        # Configure grid weights to allow the button to expand
        Buttonframe.grid_rowconfigure(0, weight=1)
        Buttonframe.grid_columnconfigure(0, weight=1)

        presbutton=Button(Buttonframe,command=self.prescription,fg='white',bg='green',font=('times new roman',12,'bold'),text='Prescription',width=22,height=13,padx=20,pady=10)
        presbutton.grid(row=0,column=0)

        prdabutton=Button(Buttonframe,text='Prescription Data ',command=self.presdata,fg='white',bg='green',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        prdabutton.grid(row=0,column=1)

        updbutton=Button(Buttonframe,text='Update',command=self.update_data,fg='white',bg='green',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        updbutton.grid(row=0,column=2)

        delbutton=Button(Buttonframe,command=self.delete,text='Delete',fg='white',bg='green',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        delbutton.grid(row=0,column=3)

        clebutton=Button(Buttonframe,command=self.clear,text='Clear',fg='white',bg='green',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        clebutton.grid(row=0,column=4)

        exitbutton=Button(Buttonframe,command=self.exit,text='Exit',fg='white',bg='green',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        exitbutton.grid(row=0,column=5)
        #================lower frame for details=====================
        Detailsframe=Frame(self.root,bd=20,relief='ridge')
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #================setting labels for left sub dataframe====================
        tablet=Label(leftframe,text='Names of Tablet',padx=2,pady=6,font=('times new roman',12,'bold'))
        tablet.grid(row=0,column=0)

        # In Tkinter, a Combobox is a widget that combines a drop-down list and
        # an entry field. It allows users to select an item from a list of options 
        # or enter their own value. This makes it a versatile widget for situations
        # where you want to provide a predefined set of choices while also allowing for custom input.

        tabletName=ttk.Combobox(leftframe,textvariable=self.nameoftablets,font=('times new roman',12,'bold'),width=33)
        tabletName['values']=("Nice",'Corona Vaccine','Acetaminophen',"Adderall","Amiodipine",'Ativan')
        tabletName.grid(row=0,column=1)

        #label and entry widget

        reflabel=Label(leftframe,text='Reference Number ',padx=2,font=('times new roman',12,'bold'))
        reflabel.grid(row=1,column=0,sticky=W)
        refent=Entry(leftframe,font=('times new roman',12,'bold'),textvariable=self.ref,width=35)
        refent.grid(row=1,column=1)

        doselabel=Label(leftframe,text='Dosage ',padx=2,pady=4,font=('times new roman',12,'bold'))
        doselabel.grid(row=2,column=0,sticky=W)
        doseent=Entry(leftframe,textvariable=self.dose,font=('times new roman',12,'bold'),width=35)
        doseent.grid(row=2,column=1)

        notlabel=Label(leftframe,text='Number of tablets ',padx=2,pady=6,font=('times new roman',12,'bold'))
        notlabel.grid(row=3,column=0,sticky=W)
        notent=Entry(leftframe,textvariable=self.nooftablets,font=('times new roman',12,'bold'),width=35)
        notent.grid(row=3,column=1)

        lotlabel=Label(leftframe,text='Lot Number ',padx=2,pady=6,font=('times new roman',12,'bold'))
        lotlabel.grid(row=4,column=0,sticky=W)
        lotent=Entry(leftframe,textvariable=self.lot,font=('times new roman',12,'bold'),width=35)
        lotent.grid(row=4,column=1)

        isslabel=Label(leftframe,text='Issue Date ',padx=2,pady=6,font=('times new roman',12,'bold'))
        isslabel.grid(row=5,column=0,sticky=W)
        issent=Entry(leftframe,textvariable=self.issuedate,font=('times new roman',12,'bold'),width=35)
        issent.grid(row=5,column=1)

        explabel=Label(leftframe,text='Expiry Date ',padx=2,pady=6,font=('times new roman',12,'bold'))
        explabel.grid(row=6,column=0,sticky=W)
        expent=Entry(leftframe,textvariable=self.expdate,font=('times new roman',12,'bold'),width=35)
        expent.grid(row=6,column=1)

        dailabel=Label(leftframe,text='Daily Dose ',padx=2,pady=6,font=('times new roman',12,'bold'))
        dailabel.grid(row=7,column=0,sticky=W)
        daient=Entry(leftframe,textvariable=self.dailydose,font=('times new roman',12,'bold'),width=35)
        daient.grid(row=7,column=1)

        sidlabel=Label(leftframe,text='Side effect ',padx=2,pady=6,font=('times new roman',12,'bold'))
        sidlabel.grid(row=8,column=0,sticky=W)
        sident=Entry(leftframe,textvariable=self.sideeffect,font=('times new roman',12,'bold'),width=35)
        sident.grid(row=8,column=1)

        infolabel=Label(leftframe,text='Further Information ',padx=2,pady=6,font=('times new roman',12,'bold'))
        infolabel.grid(row=0,column=2,sticky=W)
        infoent=Entry(leftframe,textvariable=self.furtherinfo,font=('times new roman',12,'bold'),width=35)
        infoent.grid(row=0,column=3)

        blolabel=Label(leftframe,text='Blood Pressure ',padx=2,pady=6,font=('times new roman',12,'bold'))
        blolabel.grid(row=1,column=2,sticky=W)
        bloent=Entry(leftframe,textvariable=self.bloodpressure,font=('times new roman',12,'bold'),width=35)
        bloent.grid(row=1,column=3)

        stolabel=Label(leftframe,text='Storage ',padx=2,pady=6,font=('times new roman',12,'bold'))
        stolabel.grid(row=2,column=2,sticky=W)
        stoent=Entry(leftframe,textvariable=self.storage,font=('times new roman',12,'bold'),width=35)
        stoent.grid(row=2,column=3)

        medlabel=Label(leftframe,text='Medicine',padx=2,pady=6,font=('times new roman',12,'bold'))
        medlabel.grid(row=3,column=2,sticky=W)
        medent=Entry(leftframe,textvariable=self.howtousemedication,font=('times new roman',12,'bold'),width=35)
        medent.grid(row=3,column=3)

        pidlabel=Label(leftframe,text='Patient ID ',padx=2,pady=6,font=('times new roman',12,'bold'))
        pidlabel.grid(row=4,column=2,sticky=W)
        pident=Entry(leftframe,textvariable=self.patientid,font=('times new roman',12,'bold'),width=35)
        pident.grid(row=4,column=3)

        pnalabel=Label(leftframe,text='Patient Name ',padx=2,pady=6,font=('times new roman',12,'bold'))
        pnalabel.grid(row=5,column=2,sticky=W)
        pnaent=Entry(leftframe,textvariable=self.patientname,font=('times new roman',12,'bold'),width=35)
        pnaent.grid(row=5,column=3)

        doblabel=Label(leftframe,text='Date of Birth ',padx=2,pady=6,font=('times new roman',12,'bold'))
        doblabel.grid(row=6,column=2,sticky=W)
        dobent=Entry(leftframe,textvariable=self.dateofbirth,font=('times new roman',12,'bold'),width=35)
        dobent.grid(row=6,column=3)

        padlabel=Label(leftframe,text='Patient Address ',padx=2,pady=6,font=('times new roman',12,'bold'))
        padlabel.grid(row=7,column=2,sticky=W)
        padent=Entry(leftframe,textvariable=self.patientaddress,font=('times new roman',12,'bold'),width=35)
        padent.grid(row=7,column=3)

        doclabel=Label(leftframe,text="Doctor's Name ",padx=2,pady=6,font=('times new roman',12,'bold'))
        doclabel.grid(row=8,column=2,sticky=W)
        docent=Entry(leftframe,textvariable=self.doctorname,font=('times new roman',12,'bold'),width=35)
        docent.grid(row=8,column=3)

        #prescription 
        self.pres=Text(rightframe,width=48,height=16,padx=2,pady=6,font=('times new roman',12,'bold'))
        self.pres.grid(row=0,column=0)

        #table
        #scrollbar
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.table=ttk.Treeview(Detailsframe,column=('nameoftablets','ref','dose','nooftablets','lot','issuedate','expdate','dailydose','storage','sideeffect','pname','dob','address','dname'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.table.xview)
        scroll_y=ttk.Scrollbar(command=self.table.yview)

        self.table.heading('nameoftablets',text='Name of Tablets')
        self.table.heading('ref',text='Reference No')
        self.table.heading('dose',text='Dose')
        self.table.heading('nooftablets',text='No of Tablets')
        self.table.heading('lot',text='Lot')
        self.table.heading('issuedate',text='Issue date')
        self.table.heading('expdate',text='Exp date')
        self.table.heading('dailydose',text='Daily Dose')
        self.table.heading('storage',text='Storage')
        self.table.heading('sideeffect',text='Side Effect')
        self.table.heading('pname',text='Patient Name')
        self.table.heading('dob',text='DOB')
        self.table.heading('address',text='Address')
        self.table.heading('dname',text='Doctor Name')

        self.table['show']='headings'
        self.table.pack(fill=BOTH,expand=1)

        #setting width to columns

        self.table.column('nameoftablets',width=100)
        self.table.column('ref',width=100)
        self.table.column('dose',width=100)
        self.table.column('nooftablets',width=100)
        self.table.column('lot',width=100)
        self.table.column('issuedate',width=100)
        self.table.column('expdate',width=100)
        self.table.column('dailydose',width=100)
        self.table.column('storage',width=100)
        self.table.column('sideeffect',width=100)
        self.table.column('pname',width=100)
        self.table.column('dob',width=100)
        self.table.column('address',width=100)
        self.table.column('dname',width=100)

        self.table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    # fuctionality declaration
    def presdata(self):
        if self.nameoftablets.get()=='' or self.ref.get()=='':
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                con=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')
                cursor=con.cursor()
                cursor.execute('insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        self.nameoftablets.get(),
                        self.ref.get(),
                        self.dose.get(),
                        self.nooftablets.get(),
                        self.lot.get(),
                        self.issuedate.get(),
                        self.expdate.get(),
                        self.dailydose.get(),
                        self.sideeffect.get(),
                        self.furtherinfo.get(),
                        self.bloodpressure.get(),
                        self.storage.get(),
                        self.howtousemedication.get(),
                        self.patientid.get(),
                        self.patientname.get(),
                        self.dateofbirth.get(),
                        self.patientaddress.get(),
                        self.doctorname.get()
                    ))
                # cursor.execute('select * from hospital')
                # res=cursor.fetchall()
                # for x in res:
                #     print(X)
            except my.Error as e:
                messagebox.showerror('Database Error', f'An error occurred: {e}')
            except Exception as e:
                messagebox.showerror('Error', f'An unexpected error occurred: {e}')
            finally:
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo('Success','Record has been inserted')
    def update_data(self):
        con=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')
        cursor=con.cursor()
        # Prepare the base SQL statement
        sql = "UPDATE hospital SET "
        updates = []
        values = []

        # Check each field and add to the update list if it has a new value
        if self.nameoftablets.get():
            updates.append("Name_of_tablets=%s")
            values.append(self.nameoftablets.get())
        if self.dose.get():
            updates.append("Dose=%s")
            values.append(self.dose.get())
        if self.nooftablets.get():
            updates.append("No_of_tablets=%s")
            values.append(self.nooftablets.get())
        if self.lot.get():
            updates.append("Lot_No=%s")
            values.append(self.lot.get())
        if self.issuedate.get():
            updates.append("Issue_Date=%s")
            values.append(self.issuedate.get())
        if self.expdate.get():
            updates.append("Expiry_Date=%s")
            values.append(self.expdate.get())
        if self.dailydose.get():
            updates.append("Daily_Dose=%s")
            values.append(self.dailydose.get())
        if self.sideeffect.get():
            updates.append("Side_Effect=%s")
            values.append(self.sideeffect.get())
        if self.furtherinfo.get():
            updates.append("Further_Info=%s")
            values.append(self.furtherinfo.get())
        if self.bloodpressure.get():
            updates.append("Blood_Pressure=%s")
            values.append(self.bloodpressure.get())
        if self.storage.get():
            updates.append("Storage=%s")
            values.append(self.storage.get())
        if self.howtousemedication.get():
            updates.append("Medication=%s")
            values.append(self.howtousemedication.get())
        if self.patientid.get():
            updates.append("Patient_ID=%s")
            values.append(self.patientid.get())
        if self.patientname.get():
            updates.append("Patient_Name=%s")
            values.append(self.patientname.get())
        if self.dateofbirth.get():
            updates.append("Date_of_Birth=%s")
            values.append(self.dateofbirth.get())
        if self.patientaddress.get():
            updates.append("Patient_Address=%s")
            values.append(self.patientaddress.get())
        if self.doctorname.get():
            updates.append("Doctor_Name=%s")
            values.append(self.doctorname.get())

        # Check if there are any fields to update
        if not updates:
            messagebox.showinfo('Info', 'No fields to update.')
            return

        # Join the updates and add the WHERE clause
        sql += ", ".join(updates) + " WHERE Reference_no=%s"
        values.append(self.ref.get())  # Assuming this is the Reference_no

        # Execute the update
        cursor.execute(sql, values)
        # cursor.execute('update hospital set Name_of_tablets=%s,Reference_no=%s,Dose=%s,No_of_tablets=%s,Lot_No=%s,\
        #                Issue_Date=%s,Expiry_Date=%s,Daily_Dose=%s,Side_Effect=%s,Further_Info=%s,Blood_Pressure=%s,\
        #         Storage=%s,Medication=%s,Patient_ID=%s,Patient_Name=%s,Date_of_Birth=%s,Patient_Address=%s,Doctor_Name=%s\
        #                where Reference_no=%s',(self.nameoftablets.get(),self.ref.get(),self.dose.get(),self.nooftablets.get(),
        #     self.lot.get(),
        #     self.issuedate.get(),
        #     self.expdate.get(),
        #     self.dailydose.get(),
        #     self.sideeffect.get(),
        #     self.furtherinfo.get(),
        #     self.bloodpressure.get(),
        #     self.storage.get(),
        #     self.howtousemedication.get(),
        #     self.patientid.get(),
        #     self.patientname.get(),
        #     self.dateofbirth.get(),
        #     self.patientaddress.get(),
        #     self.doctorname.get(),
        #       # Assuming this is the Reference_no
        # ))
        
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo('Success','Record has been updated')
    def fetch_data(self):
        con=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')
        cursor=con.cursor()
        cursor.execute('select * from hospital')
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert('',END,values=i)
            con.commit()
        con.close()
    def get_cursor(self,event=''):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        row=content['values']
        self.nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.nooftablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.sideeffect.set(row[8])
        self.furtherinfo.set(row[9])
        self.bloodpressure.set(row[10])
        self.storage.set(row[11])
        self.howtousemedication.set(row[12])
        self.patientid.set(row[13])
        self.patientname.set(row[14])
        self.dateofbirth.set(row[15])
        self.patientaddress.set(row[16])
        self.doctorname.set(row[17])
    def prescription(self):
        self.pres.insert(END,'Name of Tablets :\t\t\t'+self.nameoftablets.get()+'\n')
        self.pres.insert(END,'Reference No :\t\t\t'+self.ref.get()+'\n')
        self.pres.insert(END,'Dosage :\t\t\t'+self.dose.get()+'\n')
        self.pres.insert(END,'No. of Tablets :\t\t\t'+self.nooftablets.get()+'\n')
        self.pres.insert(END,'Lot :\t\t\t'+self.lot.get()+'\n')
        self.pres.insert(END,'Issue Date :\t\t\t'+self.issuedate.get()+'\n')
        self.pres.insert(END,'Expiry Date :\t\t\t'+self.expdate.get()+'\n')
        self.pres.insert(END,'Daily Dose :\t\t\t'+self.dailydose.get()+'\n')
        self.pres.insert(END,'Side Effect :\t\t\t'+self.sideeffect.get()+'\n')
        self.pres.insert(END,'Further Info :\t\t\t'+self.furtherinfo.get()+'\n')
        self.pres.insert(END,'Blood Pressure :\t\t\t'+self.bloodpressure.get()+'\n')
        self.pres.insert(END,'Storage :\t\t\t'+self.storage.get()+'\n')
        self.pres.insert(END,'Medication :\t\t\t'+self.howtousemedication.get()+'\n')
        self.pres.insert(END,'Patient ID :\t\t\t'+self.patientid.get()+'\n')
        self.pres.insert(END,'Patient Name :\t\t\t'+self.patientname.get()+'\n')
        self.pres.insert(END,'DOB :\t\t\t'+self.dateofbirth.get()+'\n')
        self.pres.insert(END,'Patient Address :\t\t\t'+self.patientaddress.get()+'\n')
        self.pres.insert(END,'Doctor Name :\t\t\t'+self.doctorname.get()+'\n')
    def delete(self):
        con=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')
        cursor=con.cursor()
        cursor.execute('delete from hospital WHERE Reference_no=%s',(self.ref.get(),))
        con.commit()
        con.close()
        # Check how many rows were affected
        # if cursor.rowcount == 0:
        #     messagebox.showinfo('Info', 'No records were deleted. Check the Reference_no.')
        # else:
        #     messagebox.showinfo('Delete', 'Patient Record has been deleted successfully')
        #     self.fetch_data()  # Refresh the displayed data
        self.fetch_data()
        messagebox.showinfo('Delete','Patient Record has been deleted successfully')
    def clear(self):
        self.nameoftablets.set('')
        self.ref.set('')
        self.dose.set('')
        self.nooftablets.set('')
        self.lot.set('')
        self.issuedate.set('')
        self.expdate.set('')
        self.dailydose.set('')
        self.sideeffect.set('')
        self.furtherinfo.set('')
        self.bloodpressure.set('')
        self.storage.set('')
        self.howtousemedication.set('')
        self.patientid.set('')
        self.patientname.set('')
        self.dateofbirth.set('')
        self.patientaddress.set('')
        self.doctorname.set('')
        self.pres.delete('1.0',END)

    def exit(self):
        exit=messagebox.askyesno('Hospital Management System',"Confirm you want to exit")
        if exit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()