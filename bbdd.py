from operator import truediv
from tkinter import *
import json

programa = Tk()
programa.title("BBDD")

##------------------ VENTANA PRINCIPAL

ventanaPrincipal = Frame(programa)
ventanaPrincipal.pack()
##------------------- "CSS"
labelwidth = 15
##------------------- VENTANA CREAR CLIENTE
def crear():
    ventanaNuevo = Tk()
    ## -------- FORMA VENTANA CREAR CLIENTE:
    #----------Linea 0 - IMAGEN CORPORATIVA (PROB DE PERRO)

    #----------Linea 1 - CLIENTE
    nombreLabel = Label(ventanaNuevo, text="Nombre cliente :", anchor="e",width=labelwidth)
    nombreLabel.grid(row=1, column=0,sticky="nesw")
    
    nombreEntry = Entry(ventanaNuevo,width=labelwidth*4)
    nombreEntry.grid(row=1,column=1, columnspan=4,sticky="nesw")

    dirLabel = Label(ventanaNuevo, text="Direccion :", anchor="e",width=labelwidth)
    dirLabel.grid(row=1, column=5,sticky="nesw")

    dirEntry = Entry(ventanaNuevo,width=labelwidth*4)
    dirEntry.grid(row=1, column=6, columnspan=4,sticky="nesw")
    #----------Linea 2 - CLIENTE
    movilLabel = Label(ventanaNuevo, text="Movil :", anchor="e",width=labelwidth)
    movilLabel.grid(row=2, column=0,sticky="nesw")

    movilEntry = Entry(ventanaNuevo,width=labelwidth*4)
    movilEntry.grid(row=2, column=1, columnspan=4,sticky="nesw")

    tlfLabel = Label(ventanaNuevo, text="TLF :", anchor="e",width=labelwidth)
    tlfLabel.grid(row=2, column=5,sticky="nesw")

    tlfEntry = Entry(ventanaNuevo,width=labelwidth*4)
    tlfEntry.grid(row=2, column=6, columnspan=4,sticky="nesw")

    #----------Linea 3 - PERRO 
    nperroLabel = Label(ventanaNuevo, text="Nombre Perro :", anchor="e",width=labelwidth)
    nperroLabel.grid(row=3,column=0,sticky="nesw")
    
    nperroEntry = Entry(ventanaNuevo,width=labelwidth*3)
    nperroEntry.grid(row=3, column=1, columnspan=3,sticky="nesw")

    eperroLabel = Label(ventanaNuevo, text="Edad :", anchor="e",width=labelwidth)
    eperroLabel.grid(row=3, column=5,sticky="nesw")

    eperroEntry = Entry(ventanaNuevo,width=labelwidth)
    eperroEntry.grid(row=3,column=6,sticky="nesw")

    pperroLabel = Label(ventanaNuevo, text="Peso :", anchor="e",width=labelwidth)
    pperroLabel.grid(row=3, column=7,sticky="nesw")

    pperroEntry = Entry(ventanaNuevo,width=labelwidth)
    pperroEntry.grid(row=3,column=8,sticky="nesw")

    #----------Linea 4 - PERRO 
    rperroLabel = Label(ventanaNuevo, text="Raza :", anchor="e",width=labelwidth)
    rperroLabel.grid(row=4, column=0,sticky="nesw")

    rperroEntry = Entry(ventanaNuevo,width=labelwidth*2)
    rperroEntry.grid(row=4, column=1, columnspan=2,sticky="nesw")

    tiempoLabel = Label(ventanaNuevo,text="Tiempo estimado :", anchor="e",width=labelwidth)
    tiempoLabel.grid(row=4, column=5,sticky="nesw")

    tiempoEntry = Entry(ventanaNuevo,width=labelwidth*2)
    tiempoEntry.grid(row=4, column=6, columnspan=2,sticky="nesw")

    #----------Linea 5 - COMENTARIOS ADICIONALES

    comentariosText= Text(ventanaNuevo,width=labelwidth*7, height=5)
    comentariosText.grid(row=5,column=0, columnspan=9,sticky="nesw")

    comentariosScroll = Scrollbar(ventanaNuevo,command=comentariosText.yview)
    comentariosScroll.grid(row=5,column=9,sticky="nesw")
    comentariosText.config(yscrollcommand=comentariosScroll.set)
    #----------Linea 6 - CONTROLES

    guardaButton = Button(ventanaNuevo, text="Guardar", width=labelwidth*2, command=lambda:Guardar())
    guardaButton.grid(row=6, column=3, columnspan=2)

    cancelButton = Button(ventanaNuevo, text="Cancelar", width=labelwidth*2, command=lambda:Cerrar(ventanaNuevo))
    cancelButton.grid(row=6,column=5, columnspan=2)
    
    ## ---- FUNCION DE GUARDAR:
    def Guardar():
        datos = [nombreEntry.get(), dirEntry.get() ,movilEntry.get(),tlfEntry.get(),nperroEntry.get(),eperroEntry.get(),pperroEntry.get(),rperroEntry.get(),tiempoEntry.get(),comentariosText.get("1.0","end-1c")]
        keyname = str(datos[4]) + "_" + str(datos[5]) + "_" + str(datos[0])
        with open('data.json', "r") as f:
            data = json.load(f)
        data[keyname]={'Ncliente': datos[0], 'Dcliente': datos[1], 'Movil': datos[2], 'Telefono': datos[3],'Nperro': datos[4], 'Eperro': datos[5], 'Peso': datos[6], 'Raza': datos[7],'Tiempo': datos[8], 'Comentarios': datos[9]}
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        Cerrar(ventanaNuevo)



##------------------- VENTANA BUSCAR CLIENTE


def buscar():
    ventanaBusqueda = Tk()
    # -------- FORMA VENTANA BUSCAR CLIENTE:
    nuevAbutton = Button(ventanaBusqueda, text="Nueva", width=20)
    nuevAbutton.grid(row=1, column=0, padx=5, pady=(20, 1))
    salir2button = Button(ventanaBusqueda, text="Cerrar", command=lambda: Cerrar(ventanaBusqueda))
    salir2button.grid(row=1, column=1, padx=5, pady=(20, 1))


##------------------- FUNCIONES DEL PROGRAMA


def Cerrar(i):
    i.destroy()


    




##------------------ CREACION VENTANA PRINCIPAL

nuevobutton = Button(ventanaPrincipal, text="Nuevo", width=20, command=lambda: crear())
nuevobutton.grid(row=1, column=0, padx=5, pady=(20, 1))

buscarbutton = Button(ventanaPrincipal, text="Buscar", width=20, command=lambda: buscar())
buscarbutton.grid(row=1, column=1, padx=5, pady=(20, 1))

salirbutton = Button(ventanaPrincipal, text="Salir", width=43, command=lambda: Cerrar(programa))
salirbutton.grid(row=2, column=0, padx=5, pady=(5, 20), columnspan=2)


programa.mainloop()
