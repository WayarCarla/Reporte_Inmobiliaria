from tkinter import *
from tkinter import ttk
from tkinter import BOTTOM,RIGHT,X,Y,Scrollbar,VERTICAL,HORIZONTAL,messagebox
from turtle import width
import tkinter as tk
from menu import propiedad
import pandas as pd

   
class VENTANA(Frame):

    propiedades = propiedad()

    def __init__(self,master=None):
        super().__init__(master)
        self.master.columnconfigure(0,weight=1)#
        self.master.rowconfigure(0,weight=1)#
        self.master.rowconfigure(1,weight=5)#
        self.master=master
        self.create_widgets()
        self.llenadatos()
        self.habilitarcajas("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarbtnguardar("disabled")
        self.Id_Propiedad=-1
        

    def habilitarcajas(self,estado):
        self.txtIdtipo.configure(state=estado)
        self.txtIdestado.configure(state=estado)
        self.txtIdopcom.configure(state=estado)
        self.txtIdprop.configure(state=estado)
        self.txtdir.configure(state=estado)
        self.txtlocalidad.configure(state=estado)
        self.txtprovincia.configure(state=estado)


    def habilitarbtnoperaciones(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
    def habilitarbtnguardar(self,estado):
        self.btnguardar.configure(state=estado)
        self.btncancelar.configure(state=estado)
      
    def limpiarcajas(self):
        self.txtIdtipo.delete(0,END)
        self.txtIdestado.delete(0,END)
        self.txtIdopcom.delete(0,END)
        self.txtIdprop.delete(0,END)
        self.txtdir.delete(0,END)
        self.txtlocalidad.delete(0,END)
        self.txtprovincia.delete(0,END)
   
    
    def limpiargrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
      
    def llenadatos(self):
        datos= self.propiedades.consulta_propiedades()
        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    
    def fNuevo (self):
        self.habilitarcajas("normal")
        self.habilitarbtnoperaciones("disabled")
        self.habilitarbtnguardar("normal")
        self.limpiarcajas()
        self.txtIdtipo.focus()
    
    def fGuardar (self):
        if self.Id_Propiedad == -1:
            self.propiedades.inserta_propiedad(self.txtIdtipo.get(),self.txtIdestado.get(),self.txtIdopcom.get(), self.txtIdprop.get(), self.txtdir.get(),self.txtlocalidad.get(),self.txtprovincia.get())
            
        else:
            print("Error")
            self.propiedades.modifica_propiedad(self.Id_Propiedad,self.txtIdtipo.get(),self.txtIdestado.get(),self.txtIdopcom.get(), self.txtIdprop.get(), self.txtdir.get(),self.txtlocalidad.get(),self.txtprovincia.get())                           
            self.Id_Propiedad = -1
            print("aqui")
        self.limpiargrid()
        self.llenadatos()
        self.limpiarcajas()
        self.habilitarbtnguardar("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarcajas("disabled")
    
    def fModificar (self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')    
        if clave == '':
            messagebox.showwarning("MODIFICAR",'SELECCIONAR UNA PROPIEDAD A MODIFICAR')
        else:
            self.Id_Propiedad = self.grid.item(selected, 'text')  
            print(self.Id_Propiedad)#####################aqui agregue
            self.habilitarcajas("normal")
            valores =self.grid.item(selected,'values')
            print(valores)######################
            self.limpiarcajas()
            self.txtIdtipo.insert(0,valores[0])
            self.txtIdestado.insert(0,valores[1])
            self.txtIdopcom.insert(0,valores[2])
            self.txtIdprop.insert(0,valores[3])
            self.txtdir.insert(0,valores[4])
            self.txtlocalidad.insert(0,valores[5])
            self.txtprovincia.insert(0,valores[6])
            self.habilitarbtnoperaciones("disabled")
            self.habilitarbtnguardar("normal")
            self.txtIdtipo.focus()
            print(self.txtIdtipo)########
            print(self.txtIdestado)
            print(self.txtIdopcom)
            print(self.txtIdprop)
            print(self.txtdir)
            print(self.txtlocalidad)
            print(self.txtprovincia)
            

    def fEliminar (self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')    
        if clave == '':
            messagebox.showwarning("ELIMINAR",'DEBE HACER CLICK EN LA PROPIEDAD A ELIMINAR')
        else:
            valores =self.grid.item(selected,'values')
            data = str(clave) #+ "," + valores [7] 
            r = messagebox.askquestion("ELIMINAR", '¿REALMENTE DESEA ELIMINAR LA PROPIEDAD?\n' + data)
            if r == messagebox.YES:
                n = self.propiedades.elimina_propiedad(clave)
                if n == 1 :
                    messagebox.showinfo("ELIMINAR",'LA PROPIEDAD AH SIDO ELIMINADA ')
                    self.limpiargrid()
                    self.llenadatos()
                else:
                    messagebox.showinfo("ELIMINAR",'ERROR -NO FUE POSIBLE ELIMINAR LA PROPIEDAD') 
    
    def fCancelar (self):
        self.limpiarcajas()
        self.habilitarbtnguardar("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarcajas("disabled")

    
    def fListatotal (self):
        self.propiedades.listarPropiedades()          

    def fDventa (self):
        self.propiedades.listarPropiedadesventa()
        
    def fDalq (self):
        self.propiedades.listarPropiedadesalquiler()

    def fVen (self):
        self.propiedades.listarPropiedadesvendidas()

    def fAlq (self):
        self.propiedades.listarPropiedadesalquiladas()
    #############################################################3
    def fGuardar_exel(self):
        #self.limpiargrid()
        datos= self.propiedades.consulta_propiedades()
        print(datos)
        i=-1
        Propiedad,Tipo,Estado,Operacion_comercial,Propietario,Direccion,Localidad,Provincia=[],[],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            Propiedad.append(datos[i][0])
            Tipo.append(datos[i][1])
            Estado.append(datos[i][2])
            Operacion_comercial.append(datos[i][3])
            Propietario.append(datos[i][4])
            Direccion.append(datos[i][5])
            Localidad.append(datos[i][6])
            Provincia.append(datos[i][7])
        datos={'Propiedad':Propiedad, 'Tipo':Tipo,'Estado':Estado,'Operacion_comercial':Operacion_comercial,'Propietario':Propietario,'Direccion':Direccion,'Localidad':Localidad,'Provincia':Provincia}
        df=pd.DataFrame(datos,columns=["Propiedad", "Tipo", "Estado", "Operacion_comercial", "Propietario", "Direccion","Localidad", "Provincia"])
        df.to_excel(f"DATOS.xlsx")
        messagebox.showinfo("GUARDAR","DATOS GUARDADOS")
        
        

    def create_widgets(self):
        self.frame_uno = Frame(self.master,bg="lightblue",width=800,height=200)#2222222
        self.frame_uno.grid(row=0,column=0,sticky="nsew")
        self.frame_dos = Frame(self.master,bg="white",width=800,height=300)
        self.frame_dos.grid(row=1,column=0,sticky="nsew")
        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Label(self.frame_uno,text="OPCIONES", bg="lightblue",fg="black",font=("Arial Black",13,"bold")).grid(column=2,row=0)
        Label(self.frame_uno,text="AGREGAR Y ACTUALIZAR DATOS DE LAS PROPIEDADES", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(columnspan=2,column=0,row=0,pady=5)

        self.btnNuevo=Button(self.frame_uno,text="INGRESAR ", command=self.fNuevo)
        self.btnNuevo.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnNuevo.grid(column=2,row=1,pady=5,padx=5)
        
  

        self.btnModificar=Button(self.frame_uno,text="MODIFICAR ", command=self.fModificar)
        self.btnModificar.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnModificar.grid(column=2,row=2,pady=5,padx=5)

        self.btnEliminar=Button(self.frame_uno,text="ELIMINAR ", command=self.fEliminar)
        self.btnEliminar.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnEliminar.grid(column=2,row=3,pady=5,padx=5)

        self.btnlistatotal=Button(self.frame_uno,text=" PROPIEDADES", command=self.fListatotal)
        self.btnlistatotal.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnlistatotal.grid(column=2,row=4,pady=5,padx=5)

        self.btndventa=Button(self.frame_uno,text=" PARA VENTA", command=self.fDventa)
        self.btndventa.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btndventa.grid(column=2,row=5,pady=5,padx=5)

        self.btndalq=Button(self.frame_uno,text="EN ALQUILER", command=self.fDalq)
        self.btndalq.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btndalq.grid(column=2,row=6,pady=6,padx=5)

        self.btnvendidas=Button(self.frame_uno,text="VENDIDAS", command=self.fVen)
        self.btnvendidas.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnvendidas.grid(column=2,row=7,pady=5,padx=5)

        self.btnalqui=Button(self.frame_uno,text="ALQUILADAS", command=self.fAlq)
        self.btnalqui.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnalqui.grid(column=2,row=8,pady=5,padx=5)

        self.btnalqui=Button(self.frame_uno,text="EXCEL", command=self.fGuardar_exel)
        self.btnalqui.config(font=("Arial",9,"bold"),fg="black", width=20, bd=3)
        self.btnalqui.grid(column=2,row=9,pady=5,padx=5)

        ###############LABEL #############

        Label(self.frame_uno,text=" TIPO ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=1,pady=5)
        Label(self.frame_uno,text=" ESTADO ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=2,pady=5)
        
        Label(self.frame_uno,text=" OPERACION COMERCIAL ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=3,pady=5)
        
        Label(self.frame_uno,text=" PROPIETARIO ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=4,pady=5)
        
        Label(self.frame_uno,text=" DIRECCION ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=5,pady=5)
        
        Label(self.frame_uno,text=" LOCALIDAD ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=6,pady=5)
        
        Label(self.frame_uno,text=" PROVINCIA ", bg="lightblue",fg="black",
            font=("Arial Black",13,"bold")).grid(column=0,row=7,pady=5)


        self.txtIdtipo=Entry(self.frame_uno)
        self.txtIdtipo.config(font=("Arial",13))
        self.txtIdtipo.grid(column=1,row=1)


        self.txtIdestado=Entry(self.frame_uno)
        self.txtIdestado.config(font=("Arial",13))
        self.txtIdestado.grid(column=1,row=2)

        self.txtIdopcom=Entry(self.frame_uno)
        self.txtIdopcom.config(font=("Arial",13))
        self.txtIdopcom.grid(column=1,row=3)

        self.txtIdprop=Entry(self.frame_uno)
        self.txtIdprop.config(font=("Arial",13))
        self.txtIdprop.grid(column=1,row=4)

        self.txtdir=Entry(self.frame_uno)
        self.txtdir.config(font=("Arial",13))
        self.txtdir.grid(column=1,row=5)

     
        self.txtlocalidad=Entry(self.frame_uno)
        self.txtlocalidad.config(font=("Arial",13))
        self.txtlocalidad.grid(column=1,row=6)
        
      
        self.txtprovincia=Entry(self.frame_uno)
        self.txtprovincia.config(font=("Arial",13))
        self.txtprovincia.grid(column=1,row=7)



        self.btnguardar=Button(self.frame_uno,text="GUARDAR", command=self.fGuardar)
        self.btnguardar.config(font=("Arial",13,"bold"),bg="green",fg="black", width=20, bd=3)
        self.btnguardar.grid(column=0,row=8,pady=5,padx=5)
            

        self.btncancelar=Button(self.frame_uno,text="CANCELAR", command=self.fCancelar)
        self.btncancelar.config(font=("Arial",13,"bold"),bg="red",fg="black", width=20, bd=3)
        self.btncancelar.grid(column=1,row=8,pady=5,padx=5)

        
        estilo_tabla=ttk.Style()
        estilo_tabla.configure("Treeview",font=("Arial",13,"bold"),foreground="black",background="white")
        estilo_tabla.map("Treeview",background=[("selected","blue")],foreground=[("selected","black")])
        estilo_tabla.configure("Heading", background="white",foreground="blue",padding=3,font=("Arial",13,"bold"))

        #self.grid = ttk.Treeview(self.frame_dos, columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.grid = ttk.Treeview(self.frame_dos, columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.grid.column("#0",width=80)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=70, anchor=CENTER)
        self.grid.column("col3",width=100, anchor=CENTER)
        self.grid.column("col4",width=140, anchor=CENTER)
        self.grid.column("col5",width=120, anchor=CENTER)
        self.grid.column("col6",width=120, anchor=CENTER)
        self.grid.column("col7",width=120, anchor=CENTER)
        self.grid.heading("#0", text="Id_Propiedad", anchor=CENTER)
        self.grid.heading("col1", text="Id_Tipo", anchor=CENTER)
        self.grid.heading("col2", text="Id_Estado", anchor=CENTER)
        self.grid.heading("col3", text="Id_Op.Comercial", anchor=CENTER)
        self.grid.heading("col4", text="Id_Propietario", anchor=CENTER)
        self.grid.heading("col5", text="DIRECCION", anchor=CENTER)
        self.grid.heading("col6", text="LOCALIDAD", anchor=CENTER)
        self.grid.heading("col7", text="PROVINCIA", anchor=CENTER)
       
        self.grid.grid(column=0,row=0,sticky="nsew") 

        ladox = ttk.Scrollbar(self.frame_dos, orient= "horizontal",command=self.grid.xview)
        ladox.grid(column=0,row=1,sticky="ew")
        ladoy=ttk.Scrollbar(self.frame_dos,orient="vertical",command=self.grid.yview)
        ladoy.grid(column=1,row=0,sticky="ns")
        self.grid.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)



        self.grid[ 'selectmode' ] = 'browse'
