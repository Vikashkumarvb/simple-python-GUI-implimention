from tkinter import *
root=Tk()
root.title('game1')
root.config(bg="#220011")
def Display(a):
    l[(a[0]-1)*10+(a[1]-1)]['text']=str((a[0])*(a[1]))
    
for i in range(1,11):
    l=Label(root,text=str(i),bg='#0022aa',relief=RAISED,fg='#ffaaaa',bd=10,font='arial 20 bold')
    l.grid(row=0,column=i,padx=7,pady=7,sticky='nesw')
for i in range(1,11):
    l=Label(root,text=str(i),bg='#0022aa',relief=RAISED,fg='#ffaaaa',bd=10,font='arial 20 bold')
    l.grid(row=i,column=0,padx=7,pady=7,sticky='nesw')
l=[]
for i in range(1,11):
    for j in range(1,11):
        l.append(Button(root,text='?',bg='#0022aa',relief=RAISED,fg='#ffaaaa',bd=10,font='arial 20 bold',command=lambda x=(i,j):Display(x)))
        l[-1].grid(row=i,column=j,padx=7,pady=7,sticky='nesw')
for i in range(11):
    
    root.grid_rowconfigure(i,weight=1)
for i in range(11):
    
    root.grid_columnconfigure(i,weight=1)
root.mainloop()
