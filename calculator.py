import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
entry=tk.Entry(root,width=20,font=("Arial",18),borderwidth=5,relief="ridge")
entry.grid(row=0,column=0,columnspan=4)

def button_click(number):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+str(number))
    
def button_clear():
    entry.delete(0,tk.END)
    
def button_equal():
    try:
        result=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
        
buttons=[('7',1,0),('8',1,1),('9',1,2),('/',1,3),('4',2,0),('5',2,1),('6',2,2),('*',2,3),('1',3,0),('2',3,1),('3',3,2),('-',3,3),('0',4,0),('.',4,1),('+',4,2),('=',4,3),]
for (text,row,col) in buttons:
    if text =="=":
        btn = tk.Button(root,text=text,padx=30,pady=20,command=button_equal)
    else:
        btn=tk.Button(root,text=text,padx=30,pady=20,command=lambda t=text: button_click(t))
    btn.grid(row=row,column=col)
        
clear_btn = tk.Button(root,text="C",padx=30,pady=20,command=button_clear)
clear_btn.grid(row=5,column=0,columnspan=4,sticky="we")

root.mainloop()
    