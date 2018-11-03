import tkinter as tk


# For scrollbar
def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

master = tk.Tk()
master.geometry('1000x1000+530+300')
#For the checkbox an radio initialising variables
v1=tk.IntVar()
v2=tk.IntVar()
v1.set(0)
v2.set(0)

#For creating multiple checkboxes
languages=[('Python',1),('C++',2),('Java',3),('JS',4),('Ruby',5),('NodeJs',6),('Machine Learning',7)]

#Creation of Scrollar

# --- create canvas with scrollbar ---

canvas = tk.Canvas(master,width=1000,height=600)
canvas.grid(sticky='E')


scrollbar = tk.Scrollbar(master, command=canvas.yview)
scrollbar.grid(sticky='E')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'

# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='ne')
    
    
#####################################


#Creation of Labels
tk.Label(frame,text="Full name : ",padx=20,pady=10).grid(row=0)
tk.Label(frame,text="Email id : ",padx=20,pady=10).grid(row=1)
tk.Label(frame,text="Mobile no. : ",padx=20,pady=10).grid(row=2)
tk.Label(frame,text="Work Experience: ",padx=20,pady=10).grid(row=3)
tk.Label(frame,text='Skills & Expertise: ',padx=20,pady=10).grid(row=4)
tk.Label(frame,text='Professional Experience: ',padx=20,pady=10).grid(row=5+len(languages))
tk.Label(frame,text='Education: ',padx=20,pady=10).grid(row=13)

#Creation of widgets prt1
entry_name = tk.Entry(frame,width=30).grid(row=0,column=1)
entry_mail = tk.Entry(frame,width=30).grid(row=1,column=1)
entry_mob = tk.Entry(frame,width=30).grid(row=2,column=1)
text_workexp = tk.Text(frame,width=30,height=10).grid(row=3,column=1)

# Creating Checkboxes
c=5
for lang,val in languages:
    tk.Checkbutton(frame,text=lang,variable=val,justify='center',padx=20,pady=10).grid(row=c,column=1,sticky='W')
    c+=1

# Creating widgets part 2
pro_exp=tk.Text(frame,width=30,height=10).grid(row=5+len(languages),column=1)
education = tk.Entry(frame,width=30).grid(row=13,column=1)


master.mainloop()
