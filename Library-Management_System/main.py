from tkinter import *
from tkinter import ttk
import mysql.connector as my
from tkinter import messagebox
import datetime

class Library:
    def __init__(self,root):
        self.root=root
        self.root.title('Library Management System')
        self.root.geometry('1530x800+0+0')
        
        self.membertype=StringVar()
        self.prnno=StringVar()
        self.title=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.address1=StringVar()
        self.address2=StringVar()
        self.postid=StringVar()
        self.mobile=StringVar()
        self.bookid=StringVar()
        self.booktitle=StringVar()
        self.author=StringVar()
        self.dateborrowed=StringVar()
        self.datedue=StringVar()
        self.days=StringVar()
        self.latereturnfine=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()

        #title for the page
        title=Label(self.root,text='LIBRARY MANAGEMENT SYSTEM',bg='light blue',fg='green',bd=20,relief='ridge',font=('times new roman',50,'bold'),padx=2,pady=6)
        title.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief='ridge',padx=20,bg='light blue')
        frame.place(x=0,y=130,width=1530,height=400)

        leftframe=LabelFrame(frame,text='Library Membership Information',bg='light blue',fg='green',bd=12,relief='ridge',font=('times new roman',20,'bold'),padx=2,pady=6)
        leftframe.place(x=0,y=5,width=900,height=370)

        Member=Label(leftframe,text='Names of Tablet',bg='light blue',textvariable='membertype',padx=2,pady=6,font=('times new roman',12,'bold'))
        Member.grid(row=0,column=0)

        # In Tkinter, a Combobox is a widget that combines a drop-down list and
        # an entry field. It allows users to select an item from a list of options 
        # or enter their own value. This makes it a versatile widget for situations
        # where you want to provide a predefined set of choices while also allowing for custom input.

        comMember=ttk.Combobox(leftframe,font=('times new roman',15,'bold'),width=27,state='readonly')
        #combo box state set to readonly i.e. can't enter any values but only select from available options
        comMember['values']=("Admin Staff","Student",'Lecturer')
        comMember.grid(row=0,column=1)

        #label and entry widget

        prn_nolabel=Label(leftframe,text='PRN Number ',padx=2,bg='light blue',font=('times new roman',12,'bold'))
        prn_nolabel.grid(row=1,column=0,sticky=W)
        prn_noent=Entry(leftframe,textvariable=self.prnno,font=('times new roman',12,'bold'),width=35)
        prn_noent.grid(row=1,column=1)

        idlabel=Label(leftframe,text='ID No ',padx=2,pady=4,bg='light blue',font=('times new roman',12,'bold'))
        idlabel.grid(row=2,column=0,sticky=W)
        ident=Entry(leftframe,textvariable=self.title,font=('times new roman',12,'bold'),width=35)
        ident.grid(row=2,column=1)

        fnamelabel=Label(leftframe,text='First Name ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        fnamelabel.grid(row=3,column=0,sticky=W)
        fnameent=Entry(leftframe,textvariable=self.firstname,font=('times new roman',12,'bold'),width=35)
        fnameent.grid(row=3,column=1)

        lnamelabel=Label(leftframe,text='Last Name ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        lnamelabel.grid(row=4,column=0,sticky=W)
        lnameent=Entry(leftframe,textvariable=self.lastname,font=('times new roman',12,'bold'),width=35)
        lnameent.grid(row=4,column=1)

        add1label=Label(leftframe,text='Address 1 ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        add1label.grid(row=5,column=0,sticky=W)
        add1ent=Entry(leftframe,textvariable=self.address1,font=('times new roman',12,'bold'),width=35)
        add1ent.grid(row=5,column=1)

        add2label=Label(leftframe,text='Address 2 ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        add2label.grid(row=6,column=0,sticky=W)
        add2ent=Entry(leftframe,textvariable=self.address2,font=('times new roman',12,'bold'),width=35)
        add2ent.grid(row=6,column=1)

        postcodelabel=Label(leftframe,text='Post Code ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        postcodelabel.grid(row=7,column=0,sticky=W)
        postcodeent=Entry(leftframe,textvariable=self.postid,font=('times new roman',12,'bold'),width=35)
        postcodeent.grid(row=7,column=1)

        mobilelabel=Label(leftframe,text='Mobile Number',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        mobilelabel.grid(row=8,column=0,sticky=W)
        mobileent=Entry(leftframe,textvariable=self.mobile,font=('times new roman',12,'bold'),width=35)
        mobileent.grid(row=8,column=1)

        bookidlabel=Label(leftframe,text='Book ID ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        bookidlabel.grid(row=0,column=2,sticky=W)
        bookident=Entry(leftframe,textvariable=self.bookid,font=('times new roman',12,'bold'),width=35)
        bookident.grid(row=0,column=3)

        booktitlelabel=Label(leftframe,text='Book Title ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        booktitlelabel.grid(row=1,column=2,sticky=W)
        booktitleent=Entry(leftframe,textvariable=self.booktitle,font=('times new roman',12,'bold'),width=35)
        booktitleent.grid(row=1,column=3)

        anamelabel=Label(leftframe,text='Author Name ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        anamelabel.grid(row=2,column=2,sticky=W)
        anameent=Entry(leftframe,textvariable=self.author,font=('times new roman',12,'bold'),width=35)
        anameent.grid(row=2,column=3)

        dateborlabel=Label(leftframe,text='Date Borrowed',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        dateborlabel.grid(row=3,column=2,sticky=W)
        dateborent=Entry(leftframe,textvariable=self.dateborrowed,font=('times new roman',12,'bold'),width=35)
        dateborent.grid(row=3,column=3)

        dateduelabel=Label(leftframe,text='Date Due ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        dateduelabel.grid(row=4,column=2,sticky=W)
        datedueent=Entry(leftframe,textvariable=self.datedue,font=('times new roman',12,'bold'),width=35)
        datedueent.grid(row=4,column=3)

        daysonlabel=Label(leftframe,text='Days on Book',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        daysonlabel.grid(row=5,column=2,sticky=W)
        daysonent=Entry(leftframe,textvariable=self.days,font=('times new roman',12,'bold'),width=35)
        daysonent.grid(row=5,column=3)

        lateretlabel=Label(leftframe,text='Late Return ',padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        lateretlabel.grid(row=6,column=2,sticky=W)
        lateretent=Entry(leftframe,textvariable=self.latereturnfine,font=('times new roman',12,'bold'),width=35)
        lateretent.grid(row=6,column=3)

        dateoverlabel=Label(leftframe,text="Date over Due",padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        dateoverlabel.grid(row=7,column=2,sticky=W)
        dateoverent=Entry(leftframe,textvariable=self.dateoverdue,font=('times new roman',12,'bold'),width=35)
        dateoverent.grid(row=7,column=3)

        apricelabel=Label(leftframe,text="Actual Price",padx=2,pady=6,bg='light blue',font=('times new roman',12,'bold'))
        apricelabel.grid(row=8,column=2,sticky=W)
        apriceent=Entry(leftframe,textvariable=self.finalprice,font=('times new roman',12,'bold'),width=35)
        apriceent.grid(row=8,column=3)

        #right frame
        rightframe=LabelFrame(frame,text='Book Details',bg='light blue',fg='green',bd=12,relief='ridge',font=('times new roman',20,'bold'),padx=2,pady=6)
        rightframe.place(x=910,y=5,width=540,height=370)

        self.txtbox=Text(rightframe,font=('times new roman',12,'bold'),width=32,height=16,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listscroll=Scrollbar(rightframe)
        listscroll.grid(row=0,column=1,sticky='ns')


        listbook=['Head first Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python Cookbook','Into Machine Learning',\
            'Machine techno','My Python','Joss Ellif guru','Elite Jungle Python','Jungli Python','Machine Python','Advance Python',\
                'Full-Stack Web Development with Python','Machine Learning & AI','Web Scraping & Automation','Cybersecurity & Ethical Hacking',\
                    'Data Science & Big Data','Python GUI Programming with Tkinter','Creating GUI Applications with PyQt and PySide']
        
        def selectBook(event=''):
            value=str(listbox.get(listbox.curselection))
            x=value
            if x=='Head first Book':
            
                self.bookid.set('BKID5454')
                self.booktitle.set("Python Manual")
                self.author.set('Paul Berry')

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.days.set(15)
                self.latereturnfine.set('Rs.50')
                self.dateoverdue.set('NO')
                self.finalprice.set("Rs.788")

        listbox=Listbox(rightframe,font=('times new roman',12,'bold'),width=20,height=16)
        listbox.bind('<<ListboxSelect>>',selectBook)
        listbox.grid(row=0,column=0,padx=4)
        listscroll.config(command=listbox.yview)

        #to display list of books in listbox
        for x in listbook:
            listbox.insert(END,x)

        #buttons frame

        Buttonframe=Frame(self.root,bd=12,relief='ridge',padx=20,bg='light blue')
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        # Configure grid weights to allow the button to expand
        Buttonframe.grid_rowconfigure(0, weight=1)
        Buttonframe.grid_columnconfigure(0, weight=1)

        adddatabutton=Button(Buttonframe,command=self.add_data,fg='white',bg='blue',font=('times new roman',12,'bold'),text='Add Data',width=22,height=13,padx=20,pady=10)
        adddatabutton.grid(row=0,column=0)

        showdatabutton=Button(Buttonframe,text='Show Data ',fg='white',bg='blue',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        showdatabutton.grid(row=0,column=1)

        updatebutton=Button(Buttonframe,text='Update Data',fg='white',bg='blue',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        updatebutton.grid(row=0,column=2)

        delbutton=Button(Buttonframe,text='Delete',fg='white',bg='blue',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        delbutton.grid(row=0,column=3)

        resetbutton=Button(Buttonframe,text='Reset',fg='white',bg='blue',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        resetbutton.grid(row=0,column=4)

        exitbutton=Button(Buttonframe,text='Exit',fg='white',bg='blue',font=('arial',12,'bold'),width=22,height=13,padx=20,pady=10)
        exitbutton.grid(row=0,column=5)

        #================lower frame for details=====================
        Detailsframe=Frame(self.root,bd=20,relief='ridge',bg='light blue')
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #table
        #scrollbar
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.table=ttk.Treeview(Detailsframe,column=('membertype','prnno','title','firstname','lastname','address1','address2','postid',\
                                                     'mobile','bookid','booktitle','author','dateborrowed','datedue','days','latereturnfine',\
                                                        'dateoverdue','finalprice'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.table.xview)
        scroll_y=ttk.Scrollbar(command=self.table.yview)

        self.table.heading('membertype',text='Member Type')
        self.table.heading('prnno',text='PRN No')
        self.table.heading('title',text='Title')
        self.table.heading('firstname',text='First Name')
        self.table.heading('lastname',text='Last Name')
        self.table.heading('address1',text='Address1')
        self.table.heading('address2',text='Address2')
        self.table.heading('postid',text='Post ID')
        self.table.heading('mobile',text='Mobile No')
        self.table.heading('bookid',text='Book ID')
        self.table.heading('booktitle',text='Book Title')
        self.table.heading('author',text='Author Name')
        self.table.heading('dateborrowed',text='Date Borrowed')
        self.table.heading('datedue',text='Date Due')
        self.table.heading('days',text='Days on Book')
        self.table.heading('latereturnfine',text='Late Return Fine')
        self.table.heading('dateoverdue',text='Date Over due')
        self.table.heading('finalprice',text='Final Price')

        self.table['show']='headings'
        self.table.pack(fill=BOTH,expand=1)

        #setting width to columns
        self.table.column('membertype',width=100)
        self.table.column('prnno',width=100)
        self.table.column('title',width=100)
        self.table.column('firstname',width=100)
        self.table.column('lastname',width=100)
        self.table.column('address1',width=100)
        self.table.column('address2',width=100)
        self.table.column('postid',width=100)
        self.table.column('mobile',width=100)
        self.table.column('bookid',width=100)
        self.table.column('booktitle',width=100)
        self.table.column('author',width=100)
        self.table.column('dateborrowed',width=100)
        self.table.column('datedue',width=100)
        self.table.column('days',width=100)
        self.table.column('latereturnfine',width=100)
        self.table.column('dateoverdue',width=100)
        self.table.column('finalprice',width=100)

    def add_data(self):
        con=my.connect(host='localhost',username='root',password='12345678',database='mydatabase')
        cursor=con.cursor()
        cursor.execute('insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        self.membertype.get(),
                        self.prnno.get(),
                        self.title.get(),
                        self.firstname.get(),
                        self.lastname.get(),
                        self.address1.get(),
                        self.address2.get(),
                        self.postid.get(),
                        self.mobile.get(),
                        self.bookid.get(),
                        self.booktitle.get(),
                        self.author.get(),
                        self.dateborrowed.get(),
                        self.datedue.get(),
                        self.days.get(),
                        self.latereturnfine.get(),
                        self.dateoverdue.get(),
                        self.finalprice.get()
                    ))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Member has been inserted successfully')

if __name__=='__main__':
    root=Tk()
    obj=Library(root)
    root.mainloop()