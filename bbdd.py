from operator import truediv
from tkinter import *

programa = Tk()
programa.title("BBDD")
programa.config(bg="blue")

##------------------ VENTANA PRINCIPAL

ventanaPrincipal = Frame(programa)
ventanaPrincipal.pack()
ventanaPrincipal.config(bg="black")

##------------------- VENTANA CREAR CLIENTE
def crear():
    ventanaNuevo = Tk()
    ventanaNuevo.config(bg="black")
    # -------- FORMA VENTANA CREAR CLIENTE:
    nuevAbutton = Button(ventanaNuevo, text="Nueva", width=20)
    nuevAbutton.grid(row=1, column=0, padx=5, pady=(20, 1))
    salir2button = Button(
        ventanaNuevo, text="Cerrar", command=lambda: Cerrar(ventanaNuevo)
    )
    salir2button.grid(row=1, column=1, padx=5, pady=(20, 1))


##------------------- VENTANA BUSCAR CLIENTE


def buscar():
    ventanaBusqueda = Tk()
    ventanaBusqueda.config(bg="black")
    # -------- FORMA VENTANA BUSCAR CLIENTE:
    nuevAbutton = Button(ventanaBusqueda, text="Nueva", width=20)
    nuevAbutton.grid(row=1, column=0, padx=5, pady=(20, 1))
    salir2button = Button(
        ventanaBusqueda, text="Cerrar", command=lambda: Cerrar(ventanaBusqueda)
    )
    salir2button.grid(row=1, column=1, padx=5, pady=(20, 1))


##------------------- FUNCIONES VENTANA PRINCIPAL


def Cerrar(i):
    i.destroy()


##------------------ CREACION VENTANA PRINCIPAL

nuevobutton = Button(ventanaPrincipal, text="Nuevo", width=20, command=lambda: crear())
nuevobutton.grid(row=1, column=0, padx=5, pady=(20, 1))

buscarbutton = Button(
    ventanaPrincipal, text="Buscar", width=20, command=lambda: buscar()
)
buscarbutton.grid(row=1, column=1, padx=5, pady=(20, 1))

salirbutton = Button(
    ventanaPrincipal, text="Salir", width=43, command=lambda: Cerrar(programa)
)
salirbutton.grid(row=2, column=0, padx=5, pady=(5, 20), columnspan=2)


programa.mainloop()
