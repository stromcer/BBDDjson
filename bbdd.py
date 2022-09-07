from operator import truediv
from tkinter import *

programa = Tk()
programa.title("BBDD")

##------------------ VENTANA PRINCIPAL

ventanaPrincipal = Frame(programa)
ventanaPrincipal.pack()

##------------------- VENTANA CREAR CLIENTE
def crear():
    ventanaNuevo = Tk()
    ## -------- FORMA VENTANA CREAR CLIENTE:
    #----------Linea 0

    #----------Linea 1
    nombreLabel = Label(ventanaNuevo, text="Nombre cliente :")
    nombreLabel.grid(row=1, column=0)
    
    nombreEntry = Entry(ventanaNuevo)
    nombreEntry.grid(row=1,column=1, columnspan=4)

    dirLabel = Label(ventanaNuevo, text="Direccion :")
    dirLabel.grid(row=1, column=5)

    dirEntry = Entry(ventanaNuevo)
    dirEntry.grid(row=1, column=6, columnspan=4)
    #----------Linea 2
    movilLabel = Label(ventanaNuevo, text="Movil :")
    movilLabel.grid(row=2, column=0)

    movilEntry = Entry(ventanaNuevo)
    movilEntry.grid(row=2, column=1, columnspan=4)

    tlfLabel = Label(ventanaNuevo, text="TLF :")
    tlfLabel.grid(row=2, column=5)

    tlfEntry = Entry(ventanaNuevo)
    tlfEntry.grid(row=2, column=6, columnspan=4)

    #----------Linea 3
    nperroLabel = Label(ventanaNuevo, text="Nombre Perro :")
    nperroLabel.grid(row=3,column=0)
    
    nperroEntry = Entry(ventanaNuevo)
    nperroEntry.grid(row=3, column=1, columnspan=3)

    eperroLabel = Label(ventanaNuevo, text="Edad :")
    eperroLabel.grid(row=3, column=5)

    eperroEntry = Entry(ventanaNuevo)
    eperroEntry.grid(row=3,column=6)

    pperroLabel = Label(ventanaNuevo, text="Peso :")
    pperroLabel.grid(row=3, column=7)

    pperroEntry = Entry(ventanaNuevo)
    pperroEntry.grid(row=3,column=8)

    #----------Linea 4
    rperroLabel = Label(ventanaNuevo, text="Raza :")
    rperroLabel.grid(row=4, column=0)

    rperroEntry = Entry(ventanaNuevo)
    rperroEntry.grid(row=4, column=1, columnspan=2)

    tiempoLabel = Label(ventanaNuevo,text="Tiempo estimado :")
    tiempoLabel.grid(row=4, column=5)

    tiempoEntry = Entry(ventanaNuevo)
    tiempoEntry.grid(row=4, column=6, columnspan=2)

    #----------Linea 5
    #----------Linea 6


##------------------- VENTANA BUSCAR CLIENTE


def buscar():
    ventanaBusqueda = Tk()
    # -------- FORMA VENTANA BUSCAR CLIENTE:
    nuevAbutton = Button(ventanaBusqueda, text="Nueva", width=20)
    nuevAbutton.grid(row=1, column=0, padx=5, pady=(20, 1))
    salir2button = Button(ventanaBusqueda, text="Cerrar", command=lambda: Cerrar(ventanaBusqueda))
    salir2button.grid(row=1, column=1, padx=5, pady=(20, 1))


##------------------- FUNCIONES VENTANA PRINCIPAL


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
