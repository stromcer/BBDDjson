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
resultado = ""
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
        with open('data.json', 'r') as f:
            data = json.load(f)
        data[keyname]={'Ncliente': datos[0], 'Dcliente': datos[1], 'Movil': datos[2], 'Telefono': datos[3],'Nperro': datos[4], 'Eperro': datos[5], 'Peso': datos[6], 'Raza': datos[7],'Tiempo': datos[8], 'Comentarios': datos[9]}
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        Cerrar(ventanaNuevo)



##------------------- VENTANA BUSCAR CLIENTE


def buscar():
    ventanaBusqueda = Tk()

    with open('.\data.json', 'r') as f:
        datab = json.load(f)
    filter = list(datab.keys())
    filterf = []

    for i in filter:
        e = i.replace("_", " con ", 1)
        e = e.replace("_", " años. Dueño : ")
        filterf.append(e)
    
    # -------- FORMA VENTANA BUSCAR CLIENTE:
    buscarLabel = Label(ventanaBusqueda, text="Buscar :",width=labelwidth)
    buscarLabel.grid(row=0,column=1)

    buscarEntry = Entry(ventanaBusqueda,width=labelwidth*2)
    buscarEntry.grid(row=0, column=2,columnspan=2)

    buscarList = Listbox(ventanaBusqueda,width=labelwidth*3)
    buscarList.grid(row=1, column= 1,columnspan=3)

    buscarButton = Button(ventanaBusqueda,width=labelwidth, text="Abrir ficha cliente", command=lambda:abrir())
    buscarButton.grid(row=2,column=2)

    cancelButton = Button(ventanaBusqueda,width=labelwidth, text="Cancelar", command=lambda:Cerrar(ventanaBusqueda))
    cancelButton.grid(row=2,column=3)

    # Boton de Mostrar resultado:
    def abrir():
        global resultado
        resultado =  str((buscarList.get(ACTIVE)))
        if resultado == "":
            pass
        else:
            resultado = filter[filterf.index(resultado)]
            vresultado()


    # -------- Filtro de busqueda
    def update(data):
        #Limpiar la listbox
        buscarList.delete(0, END)
        for i in data:
            buscarList.insert(END, i)
    
    def check(e):
        typed = buscarEntry.get()
        print(typed)

        if typed == "":
            data = filterf
        else:
            data = []
            for item in filterf:
                if typed.lower() in item.lower():
                    data.append(item)
        
        update(data)


    update(filterf)
    buscarEntry.bind("<KeyRelease>", check)
    

## ------------------ Ventana Resultado cliente:
def vresultado():
    global resultado
    ventanaResultado = Tk()
    with open("data.json", "r") as f:
        dres = json.load(f)           
    #----------Linea 0 - IMAGEN CORPORATIVA (PROB DE PERRO)

    #----------Linea 1 - CLIENTE
    rnombreLabel = Label(ventanaResultado, text="Nombre cliente :", anchor="e",width=labelwidth)
    rnombreLabel.grid(row=1, column=0,sticky="nesw")
    
    rnombreEntry = Entry(ventanaResultado,width=labelwidth*4)
    rnombreEntry.grid(row=1,column=1, columnspan=4,sticky="nesw")
    rnombreEntry.insert(0, dres[resultado]['Ncliente'])
    rnombreEntry.config(state="disabled")
 

    rdirLabel = Label(ventanaResultado, text="Direccion :", anchor="e",width=labelwidth)
    rdirLabel.grid(row=1, column=5,sticky="nesw")

    rdirEntry = Entry(ventanaResultado,width=labelwidth*4)
    rdirEntry.grid(row=1, column=6, columnspan=4,sticky="nesw")
    rdirEntry.insert(0, dres[resultado]['Dcliente'])
    rdirEntry.config(state="disabled")
    #----------Linea 2 - CLIENTE
    rmovilLabel = Label(ventanaResultado, text="Movil :", anchor="e",width=labelwidth)
    rmovilLabel.grid(row=2, column=0,sticky="nesw")

    rmovilEntry = Entry(ventanaResultado,width=labelwidth*4)
    rmovilEntry.grid(row=2, column=1, columnspan=4,sticky="nesw")
    rmovilEntry.insert(0, dres[resultado]['Movil'])
    rmovilEntry.config(state="disabled")

    rtlfLabel = Label(ventanaResultado, text="TLF :", anchor="e",width=labelwidth)
    rtlfLabel.grid(row=2, column=5,sticky="nesw")

    rtlfEntry = Entry(ventanaResultado,width=labelwidth*4)
    rtlfEntry.grid(row=2, column=6, columnspan=4,sticky="nesw")
    rtlfEntry.insert(0, dres[resultado]['Telefono'])
    rtlfEntry.config(state="disabled")

    #----------Linea 3 - PERRO 
    rnperroLabel = Label(ventanaResultado, text="Nombre Perro :", anchor="e",width=labelwidth)
    rnperroLabel.grid(row=3,column=0,sticky="nesw")
    
    rnperroEntry = Entry(ventanaResultado,width=labelwidth*3)
    rnperroEntry.grid(row=3, column=1, columnspan=3,sticky="nesw")
    rnperroEntry.insert(0, dres[resultado]['Nperro'])
    rnperroEntry.config(state="disabled")

    reperroLabel = Label(ventanaResultado, text="Edad :", anchor="e",width=labelwidth)
    reperroLabel.grid(row=3, column=5,sticky="nesw")

    reperroEntry = Entry(ventanaResultado,width=labelwidth)
    reperroEntry.grid(row=3,column=6,sticky="nesw")
    reperroEntry.insert(0, dres[resultado]['Eperro'])
    reperroEntry.config(state="disabled")

    rpperroLabel = Label(ventanaResultado, text="Peso :", anchor="e",width=labelwidth)
    rpperroLabel.grid(row=3, column=7,sticky="nesw")

    rpperroEntry = Entry(ventanaResultado,width=labelwidth)
    rpperroEntry.grid(row=3,column=8,sticky="nesw")
    rpperroEntry.insert(0, dres[resultado]['Peso'])
    rpperroEntry.config(state="disabled")

    #----------Linea 4 - PERRO 
    rrperroLabel = Label(ventanaResultado, text="Raza :", anchor="e",width=labelwidth)
    rrperroLabel.grid(row=4, column=0,sticky="nesw")

    rrperroEntry = Entry(ventanaResultado,width=labelwidth*2)
    rrperroEntry.grid(row=4, column=1, columnspan=2,sticky="nesw")
    rrperroEntry.insert(0, dres[resultado]['Raza'])
    rrperroEntry.config(state="disabled")

    rtiempoLabel = Label(ventanaResultado,text="Tiempo estimado :", anchor="e",width=labelwidth)
    rtiempoLabel.grid(row=4, column=5,sticky="nesw")

    rtiempoEntry = Entry(ventanaResultado,width=labelwidth*2)
    rtiempoEntry.grid(row=4, column=6, columnspan=2,sticky="nesw")
    rtiempoEntry.insert(0, dres[resultado]['Tiempo'])
    rtiempoEntry.config(state="disabled")

    #----------Linea 5 - COMENTARIOS ADICIONALES

    rcomentariosText= Text(ventanaResultado,width=labelwidth*7, height=5)
    rcomentariosText.grid(row=5,column=0, columnspan=9,sticky="nesw")
    rcomentariosText.insert(INSERT, dres[resultado]['Comentarios'])
    rcomentariosText.config(state="disabled")

    rcomentariosScroll = Scrollbar(ventanaResultado,command=rcomentariosText.yview)
    rcomentariosScroll.grid(row=5,column=9,sticky="nesw")
    rcomentariosText.config(yscrollcommand=rcomentariosScroll.set)
    #----------Linea 6 - CONTROLES

    rmodificarButton = Button(ventanaResultado, text="Editar", width=labelwidth*2)
    rmodificarButton.grid(row=6, column=3, columnspan=2)

    rcancelButton = Button(ventanaResultado, text="Cancelar", width=labelwidth*2, command=lambda:Cerrar(ventanaResultado))
    rcancelButton.grid(row=6,column=5, columnspan=2)

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