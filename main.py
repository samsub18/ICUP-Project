import tkinter as tk
from findandreplace import *
from PIL import ImageTk, Image


#---------FullScreenApp---------#
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 0
        self._geom = master.geometry('%sx%s' % (int(width/2), height))
        #self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom
#----------------------------------#


# Colour for everything
colour = 'gray'

# ------ Setting up the screen------------
master = tk.Tk()
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.geometry('%sx%s' % (width, height))
# master.geometry('1000x1000+530+300')
master.configure(background=colour)


# For the checkbox and radio initialising variables
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
v5 = tk.IntVar()
v6 = tk.IntVar()
v7 = tk.IntVar()
v8 = tk.IntVar()
v9 = tk.IntVar()
v10 = tk.IntVar()
v1.set(2)
v2.set(3)
v3.set(4)
v4.set(5)
v5.set(6)
v6.set(7)
v7.set(8)
v8.set(9)
v9.set(10)
v10.set(11)

# ------- Creating multiple checkboxes for skills input ------- #
languages = [('Python', v1), ('C/C++', v2), ('Java', v3), ('JavaScript', v4),
             ('Ruby', v5), ('Microsoft Office', v6), ('Machine Learning', v7), ('SAP', v8), ('Adobe Photoshop', v9), ('Social Media Marketing', v10)]


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


canvas = tk.Canvas(master, width=650, height=800)
frame = tk.Frame(canvas)
canvas.grid(sticky='E')
canvas.configure(background=colour)


# update scrollregion after starting 'mainloop'

# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

# frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='ne')
frame.configure(background=colour)


# ---------------------------------------------------------------------------------


# ----------------Creation of Labels----------
tk.Label(frame, text="Full name : ", padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=0, sticky='w')
tk.Label(frame, text="Email id : ", padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=1, sticky='w')
tk.Label(frame, text="Mobile number : ", padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=2, sticky='w')
tk.Label(frame, text="Work Experience : ", padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=3, sticky='w')
tk.Label(frame, text='Skills & Expertise: ', padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=4, sticky='w')
tk.Label(frame, text='Professional Experience : ', padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=5 + len(languages), sticky='w')
tk.Label(frame, text='Education : ', padx=20, pady=10,
         bg=colour, font=('Helvetica', 16)).grid(row=13, sticky='w')

# --------------Creation of widgets prt1--------


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if event.widget.cget('fg') == 'grey' and event.widget.type == 'entry':
        event.widget.delete(0, "end")  # delete all the text in the entry
        event.widget.insert(0, '')  # Insert blank for user input
        event.widget.config(fg='black')
    elif event.widget.cget('fg') == 'grey' and event.widget.type == 'text':
        # delete all the text in the entry
        event.widget.delete('0.0', "end")
        event.widget.insert('0.0', '')  # Insert blank for user input
        event.widget.config(fg='black')


def on_focusout(event):
    if event.widget.type == 'entry' and event.widget.get() == '':
        event.widget.insert(0, event.widget.default)
        event.widget.config(fg='grey')
    elif event.widget.type == 'text' and ord(event.widget.get(0.0)) == 10:
        event.widget.insert(0.0, event.widget.default)
        event.widget.config(fg='grey')


entry_name = tk.Entry(frame, width=30, font=('Arial', 13))
entry_name.type = 'entry'
entry_name.default = 'Enter your full name'
entry_name.insert(0, entry_name.default)
entry_name.bind('<FocusIn>', on_entry_click)
entry_name.bind('<FocusOut>', on_focusout)
entry_name.config(fg='grey')
entry_name.grid(row=0, column=1)

entry_mail = tk.Entry(frame, width=30, font=('Arial', 13))
entry_mail.type = 'entry'
entry_mail.default = 'Enter your e-mail address'
entry_mail.insert(0, entry_mail.default)
entry_mail.bind('<FocusIn>', on_entry_click)
entry_mail.bind('<FocusOut>', on_focusout)
entry_mail.config(fg='grey')
entry_mail.grid(row=1, column=1)


entry_mob = tk.Entry(frame, width=30, font=('Arial', 13))
entry_mob.type = 'entry'
entry_mob.default = 'Enter your mobile number'
entry_mob.insert(0, entry_mob.default)
entry_mob.bind('<FocusIn>', on_entry_click)
entry_mob.bind('<FocusOut>', on_focusout)
entry_mob.config(fg='grey')
entry_mob.grid(row=2, column=1)


text_workexp = tk.Text(frame, width=30, height=5, font=('Arial', 13))
text_workexp.type = 'text'
text_workexp.default = 'Describe the places you have previously worked at'
text_workexp.insert('0.0', text_workexp.default)
text_workexp.bind('<FocusIn>', on_entry_click)
text_workexp.bind('<FocusOut>', on_focusout)
text_workexp.config(fg='grey')
text_workexp.grid(row=3, column=1)

# -------- Creating Checkboxes---------
c = 4
for lang, val in languages:
    tk.Checkbutton(frame, text=lang, variable=val, justify='center', padx=20, pady=10,
                   bg=colour, font=('Helvetica', 13)).grid(row=c, column=1, sticky='W')
    c += 1

# -------------- Creating widgets part 2-------
pro_exp = tk.Text(frame, width=30, height=5, font=('Arial', 13))
pro_exp.type = 'text'
pro_exp.default = 'Describe your previous roles, projects you\'ve worked on and other interesting work experiences!'
pro_exp.insert('0.0', pro_exp.default)
pro_exp.bind('<FocusIn>', on_entry_click)
pro_exp.bind('<FocusOut>', on_focusout)
pro_exp.config(fg='grey')
pro_exp.grid(row=5 + len(languages), column=1)


education = tk.Entry(frame, width=30, font=('Arial', 13))
education.type = 'entry'
education.default = 'Mention your academic qualifications'
education.insert(0, education.default)
education.bind('<FocusIn>', on_entry_click)
education.bind('<FocusOut>', on_focusout)
education.config(fg='grey')
education.grid(row=13, column=1)


# --------------Getting the values from user----------
user_info = {}

submitted = False


def info_get():
    global submitted
    submitted = True

    user_info['XXXSKILLSXXX'] = []
    count = 0
    for lang, val in languages:
        if val.get() == 1:
            count += 1
            user_info['XXXSKILLSXXX'].append(
                str(count) + '. ' + lang + '<w:br/>')
    user_info['XXXSKILLSXXX'] = ''.join(user_info['XXXSKILLSXXX'])
    user_info['XXXNAMEXXX'] = (entry_name.get())
    user_info['XXXEMAILXXX'] = (entry_mail.get())
    user_info['XXXPHONENUMBERXXX'] = (entry_mob.get())
    user_info['XXXEDUCATIONXXX'] = (education.get())
    user_info['XXXEXPERIENCEXXX'] = text_workexp.get("1.0", 'end-1c')
    user_info['XXXPROFESSIONALEXPERIENCEXXX'] = pro_exp.get('1.0', 'end-1c')

    # Closing the input window
    master.destroy()

# --------Creating buttons for submit and quit--------


tk.Label(frame, bg=colour).grid(row=16)
tk.Button(frame, text='SUBMIT', command=info_get, font=(
    'Arial', 13)).grid(row=17, column=1, sticky='W')
tk.Button(frame, text='QUIT', command=master.destroy, font=(
    'Arial', 13)).grid(row=17, column=1, sticky='S')

#------------------------------------------------------#


#-----------Creating The Credits Button------------------------#

def credits():
    import tkinter as tk
    root = tk.Tk()
    tk.Label(root, text="Created By : \n1. Naveen: Linking Of Python Code and Word Doc, Text Input Fields \n2. Sameer: Graphical User Interface, Logo \n3. Sanjith: Combining Of code",
             padx=20, pady=10, bg=colour, font=('Helvetica', 16)).grid(row=1)
    root.mainloop()


b = tk.Button(frame, text="CREDITS", command=credits, font=('Arial', 13))
b.grid(row=17, column=1, sticky='E')

#----------------------------------------------------------------#

#-----------Adding the logo image-----------#
img = ImageTk.PhotoImage(Image.open('logo_final.png'))
res = tk.Label(master, image=img, width=int(canvas['width']) + 124, height=canvas['height'])
res.grid(row=0, column=25, padx=2, pady=1, sticky="N")

app = FullScreenApp(master)

master.mainloop()
if submitted:
    createResume(user_info)
