from tkinter import*

# Contenedor general
raiz = Tk()

#Atributos del contenedor general
raiz.title ("Datos Clima") #Defino el título de la ventana
raiz.geometry("1280x640") #Dimensiono el tamaño de la ventana
raiz.config(bg="gray") #Asigno color de fondo

# Frame contenedor de widgets (gráficos, etiquetas, botones, etc. )
miFrame = Frame(raiz)

#Empaqueto el frame dentro de la raiz
miFrame.pack(side="left", anchor="n") #'side' establece la ubicación del frame, 'anchor' define con puntos cardinales. En este caso a la izquierda y arriba

#Atributos del frame
miFrame.config(width="400", height="640") #Defino tamaño
miFrame.config(bg="green") # Defino color
miFrame.config(bd=5) # Seteo el ancho del borde del frame
miFrame.config(relief="solid") # Elijo el tipo de borde del frame
miFrame.config(cursor="hand2") # Especifico el ícono del cursor al pasar sobre el frame

#Label ubicado dentro del Frame
miLabel = Label(miFrame, text="Introduzca nombre de ciudad:", fg="gray", bg="yellow", font=("Comics Sans MS", 8)) # Con 'text' defino el texto a mostrar, con 'fg' defino el color de la fuente, con 'bg' el color de fondo
# Con 'font' establezco tipo de fuente y tamaño
#Ubico el Label dentro del Frame
miLabel.place(x=10, y=20) # Con el método 'place' defino donde ubico el Label

#Imagen ubicada dentro del Frame
miImagen = PhotoImage(file="bandera.png") #Asigno un archivo de imagen
fotoLabel = Label(miFrame, image=miImagen)
fotoLabel.place(x=55,y=300)

#Cuadro de texto ubicado dentro del Frame
miCuadroTexto = Entry(miFrame, fg="blue", justify="center").place(x=170,y=20) #Especifico que el color de la fuente sea azul
#Justifico el texto centrado mediante 'justify'

#Label clave
miLabelClave = Label(miFrame, text="Introduzca clave: ").place(x=10, y=50)

#Cuadro de texto formato clave
miCuadroClave = Entry(miFrame, show="*").place(x=170, y=50) #Con 'Show' especifico un caracter a mostrar. La entrada se toma tal cual la tecleo


#Cuadro comentarios
miLabelComentario = Label(miFrame, text="Observaciones: ").place(x=10, y=80)

#Texto
miTextoComentario = Text(miFrame, width=15, height=10, font=("Comics Sans MS",8)).place(x=170, y=80)





raiz.mainloop()