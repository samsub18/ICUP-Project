import tkinter as tk


#------ Setting up the screen------------
master = tk.Tk()
master.geometry('1000x1000+530+300')
master.configure(background='#a1dbcd')


#For the checkbox and radio initialising variables
v1=tk.IntVar()
v2=tk.IntVar()
v3=tk.IntVar()
v4=tk.IntVar()
v5=tk.IntVar()
v6=tk.IntVar()
v7=tk.IntVar()
v1.set(2)
v2.set(3)
v3.set(4)
v4.set(5)
v5.set(6)
v6.set(7)
v7.set(8)



#For creating multiple checkboxes
languages=[('Python',v1),('C++',v2),('Java',v3),('JS',v4),('Ruby',v5),('NodeJs',v6),('Machine Learning',v7)]

#-----------------------------Creation of Scrollar-------------------------

# --- create canvas with scrollbar ---
def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))



canvas = tk.Canvas(master,width=1000,height=600)
frame = tk.Frame(canvas)
canvas.grid(sticky='E')
canvas.configure(background='#a1dbcd')

scrollbar = tk.Scrollbar(master,orient="vertical", command=canvas.yview)
scrollbar.grid(sticky='E')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'

# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

#frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='ne')
frame.configure(background='#a1dbcd')
    
    
#---------------------------------------------------------------------------------


#----------------Creation of Labels----------
tk.Label(frame,text="Full name : ",padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=0)
tk.Label(frame,text="Email id : ",padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=1)
tk.Label(frame,text="Mobile no. : ",padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=2)
tk.Label(frame,text="Work Experience: ",padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=3)
tk.Label(frame,text='Skills & Expertise: ',padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=4)
tk.Label(frame,text='Professional Experience: ',padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=5+len(languages))
tk.Label(frame,text='Education: ',padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',16)).grid(row=13)

#--------------Creation of widgets prt1--------
entry_name = tk.Entry(frame,width=30,font=('Arial',13))
entry_name.grid(row=0,column=1)

entry_mail = tk.Entry(frame,width=30,font=('Arial',13))
entry_mail.grid(row=1,column=1)

entry_mob = tk.Entry(frame,width=30,font=('Arial',13))
entry_mob.grid(row=2,column=1)

text_workexp = tk.Text(frame,width=30,height=5,font=('Arial',13))
text_workexp.grid(row=3,column=1)

#-------- Creating Checkboxes---------
c=4
for lang,val in languages:
    tk.Checkbutton(frame,text=lang,variable=val,justify='center',padx=20,pady=10,bg='#a1dbcd',font=('Helvetica',13)).grid(row=c,column=1,sticky='W')
    c+=1

#-------------- Creating widgets part 2-------
pro_exp=tk.Text(frame,width=30,height=5,font=('Arial',13))
pro_exp.grid(row=5+len(languages),column=1)


education = tk.Entry(frame,width=30,font=('Arial',13))
education.grid(row=13,column=1)



#--------------Getting the values from user----------
user_info={}
def info_get():
    user_info['Languages']=[]
    for lang,val in languages:
        if val.get()==1:
            user_info['Languages'].append(lang)
            
    user_info['Name']=(entry_name.get())
    user_info['Mail']=(entry_mail.get())
    user_info['Mobile Number']=(entry_mob.get())
    user_info['Education']=(education.get())
    user_info['Work experience']=text_workexp.get("1.0",'end-1c')
    user_info['Proffesional Experience']=pro_exp.get('1.0','end-1c')


#--------Creating buttons for submit and quit--------

tk.Button(frame,text='SUBMIT',command=info_get,font=('Arial',13)).grid(row=16,column=1,sticky='W')
tk.Button(frame,text='QUIT',command=master.quit,font=('Arial',13)).grid(row=16,column=1,sticky='E')

master.mainloop()
