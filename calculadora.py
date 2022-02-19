"""
calculadora de suma,resta,mult, division
"""

from tkinter import Tk,Label,IntVar,Radiobutton,Entry,StringVar,Button

def calculos():
    valor1=float(entrada1.get())
    valor2=float(entrada2.get())
    simbolo=operacion.get()
    if simbolo==1:
        etiqueta.config(text="+")
        resultado=valor1+valor2
        etiqueta3.config(text=str(resultado))
    elif simbolo==2:
        etiqueta.config(text="-")
        resultado=valor1-valor2
        etiqueta3.config(text=str(resultado))
    elif simbolo==3:
        etiqueta.config(text="x")
        resultado=valor1*valor2
        etiqueta3.config(text=str(resultado))
    elif simbolo==4:
        etiqueta.config(text="/")
        resultado=valor1/valor2
        etiqueta3.config(text=str(resultado))
    else:
        pass
    
    
ventana=Tk()
ventana.geometry("360x200")
ventana.config(bg="#4F5688")
ventana.title("Calculadora")

ent1=StringVar()
entrada1=Entry(ventana,textvariable=ent1,width=10)
entrada1.grid(row=0,column=0)

ent2=StringVar()
entrada2=Entry(ventana,textvariable=ent2,width=10)
entrada2.grid(row=0,column=2)

etiqueta=Label(ventana,text="",bg="#4F5688",width=5,fg="white")
etiqueta.grid(row=0,column=1)
etiqueta2=Label(ventana,text="=",bg="#4F5688",width=5,fg="white")
etiqueta2.grid(row=0,column=3)
etiqueta3=Label(ventana,text="",bg="#4F5688",width=5,fg="white")
etiqueta3.grid(row=0,column=4)

operacion=IntVar()
boton1=Radiobutton(ventana,text="suma",variable=operacion,command=calculos,value=1,bg="#4F5688",fg="white")
boton1.grid(column=0,row=1)

boton2=Radiobutton(ventana,text="resta",variable=operacion,command=calculos,value=2,bg="#4F5688",fg="white")
boton2.grid(column=1,row=1)

boton3=Radiobutton(ventana,text="multiplicacion",variable=operacion,command=calculos,value=3,bg="#4F5688",fg="white")
boton3.grid(column=0,row=2)

boton4=Radiobutton(ventana,text="division",variable=operacion,command=calculos,value=4,bg="#4F5688",fg="white")
boton4.grid(column=1,row=2)
ventana.mainloop()


