from tkinter import*
import requests

# Contenedor general
raiz = Tk()

URL_API_CLIMA = "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&APPID=bbbe84df6ab458740a22a2e0a1eb7663"
nombreCiudad = StringVar()
temperaturaCiudad = StringVar()
humedadCiudad = StringVar()

#Atributos del contenedor general
raiz.title ("Datos Clima en Rafaela") #Defino el título de la ventana
raiz.geometry("1280x640") #Dimensiono el tamaño de la ventana
raiz.config(bg="gray") #Asigno color de fondo

# Frame contenedor de widgets (gráficos, etiquetas, botones, etc. )
miFrame = Frame(raiz)

#Empaqueto el frame dentro de la raiz
miFrame.pack(side="right", anchor="n") #'side' establece la ubicación del frame, 'anchor' define con puntos cardinales. En este caso a la izquierda y arriba

#Atributos del frame
miFrame.config(width="400", height="640") #Defino tamaño
#miFrame.config(bg="green") # Defino color
miFrame.config(bd=5) # Seteo el ancho del borde del frame
miFrame.config(relief="solid") # Elijo el tipo de borde del frame
miFrame.config(cursor="hand2") # Especifico el ícono del cursor al pasar sobre el frame

#Imagen ubicada dentro del Frame
miImagen = PhotoImage(file="bandera.png") #Asigno un archivo de imagen
fotoLabel = Label(miFrame, image=miImagen)
#fotoLabel.place(x=55,y=300)
fotoLabel.grid(column=0, row=4)

#Label ubicado dentro del Frame
LabelCiudad = Label(miFrame, text="Nombre ciudad:", fg="blue", font=("Arial Black", 8)) # Con 'text' defino el texto a mostrar, con 'fg' defino el color de la fuente, con 'bg' el color de fondo
# Con 'font' establezco tipo de fuente y tamaño
#Ubico el Label dentro del Frame
#miLabel.place(x=10, y=20) # Con el método 'place' defino donde ubico el Label
LabelCiudad.grid(column=0,row=0,padx=10, pady=5)

#Cuadro de texto ubicado dentro del Frame para ingresar el nombre de la ciudad
#miCuadroTexto = Entry(miFrame, fg="blue", justify="center").place(x=170,y=20) #Especifico que el color de la fuente sea azul
#Justifico el texto centrado mediante 'justify'
EntryCiudad = Entry(miFrame, fg="green", justify="center",textvariable= nombreCiudad, font=("Comics Sans MS",8)) #'fg' color de la fuente, 'justify' alienación del texto
EntryCiudad.grid(column=1, row=0, padx=10, pady=5)

LabelTemperatura = Label(miFrame, text="Temperatura °C: ", font=("Arial Black",8))
LabelTemperatura.grid(column=0, row=1, padx=10, pady=5)

EntryTemperatura = Entry(miFrame, fg="gray", justify="center",textvariable= temperaturaCiudad, font=("Comics Sans MS",8)) #'fg' color de la fuente, 'justify' alienación del texto
EntryTemperatura.grid(column=1, row=1, padx=10, pady=5)

LabelHumedad = Label(miFrame, text="Humedad %: ", font=("Arial Black",8), fg="red")
LabelHumedad.grid(column=0, row=2, padx=10, pady=5)

EntryHumedad = Entry(miFrame, fg="red", justify="center",textvariable= humedadCiudad) #'fg' color de la fuente, 'justify' alienación del texto
EntryHumedad.grid(column=1, row=2, padx=10, pady=5)


#------------------------------------------------------------------------------
#Label clave
#miLabelClave = Label(miFrame, text="Introduzca clave: ").place(x=10, y=50)

#miLabelClave = Label(miFrame, text="Introduzca clave: ")
#miLabelClave.grid(column=0, row=6, padx=10, pady=10)

#Cuadro de texto formato clave
#miCuadroClave = Entry(miFrame, show="*").place(x=170, y=50) #Con 'Show' especifico un caracter a mostrar. La entrada se toma tal cual la tecleo

#miCuadroClave = Entry(miFrame, show="*")
#miCuadroClave.grid(column=1, row=6, padx=10, pady=10)

#--------------------------------------------------------------------------------

#Etiqueta del recuadro comentarios
#miLabelComentario = Label(miFrame, text="Observaciones: ").place(x=10, y=80)
miLabelComentario = Label(miFrame, text="Observaciones: ")
miLabelComentario.grid(column=0, row=3, padx=10, pady=5)

#Texto. Tipo recuadro como para escribir comentarios u observaciones de gran longitud
#miTextoComentario = Text(miFrame, width=15, height=10, font=("Comics Sans MS",8)).place(x=170, y=80)
miTextoComentario = Text(miFrame, width=17, height=10, font=("Arial Black", 8), fg="green")
miTextoComentario.grid(column=1, row=3, padx=10, pady=5)

#Barra de desplazamiento
miScrollBar = Scrollbar(miFrame, command=miTextoComentario.yview) #'yview' establece el scrollbar en vertical
miScrollBar.grid(column=2, row=3, sticky="nsew")
#sticky = "nsew" adapta el tamaño del scrollbar al tamaño del elemento
miTextoComentario.config(yscrollcommand=miScrollBar.set) #Con este comando permito que el posicionador del scrollbar acompañe al texto


def consultaClima():
    infoClima = recuperarUrl(URL_API_CLIMA)
    ciudad = infoClima["list"][0]["name"]
    temperatura = f'{infoClima["list"][0]["main"]["temp"]:.1f}'
    humedad = infoClima["list"][0]["main"]["humidity"]
    nombreCiudad.set(ciudad)
    temperaturaCiudad.set(temperatura)
    humedadCiudad.set(humedad)


def recuperarUrl(destino):
    consulta=requests.get(destino)
    if (consulta.status_code == 200):
            return consulta.json()
    else:
        return False

    
#Botón
miBoton=Button(miFrame, text="Consultar", command= lambda:consultaClima())
miBoton.grid(column=1,row=4)



raiz.mainloop()