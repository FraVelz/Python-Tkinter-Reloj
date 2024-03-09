#* ************ ************ Importar modulos ************ ************ *#
from tkinter import Tk, Label
import time, json

#* *********** ********* Configuracion Opcional ********** *********** *#
color_texto = 'white'

#* ************ Crear y configuracion de la ventana ************ *#
ventana = Tk()
ventana.config(bg='gray')
ventana.geometry('500x200')
ventana.wm_attributes('-transparentcolor','gray')
ventana.overrideredirect(1) # Elimina el borde de la ventana

#* ************ ****** Funciones de la ventana ****** ************ *#
def salir(*args):
    ventana.destroy()
    ventana.quit()

def start(event):
    global x, y
    x = event.x
    y = event.y

def stop(event):
    global x, y
    x = None
    y = None

def mover(event):
    global x, y 
    deltax = event.x - x
    deltay = event.y - y
    ventana.geometry("+%s+%s" % (ventana.winfo_x() + deltax, ventana.winfo_y() + deltay))
    ventana.update()

#* ************ ****** Muestra la hora Actualizada ****** ************ *#

def obtener_tiempo(*args):
    hora = time.strftime('%H:%M:%S')
    zona = time.strftime('%Z')
    fecha_formato12 = time.strftime('%A' ' ' '%d' ' ' '%B' ' ' '%Y')

    texto_hora['text'] = hora
    texto_fecha12['text'] = fecha_formato12
    zona_horaria['text'] = zona
    texto_hora.after(1000, obtener_tiempo)

#* ********* Asignar las funciones de la ventana a la ventana ********* *#
ventana.bind("<ButtonPress-1>", start)
ventana.bind("<ButtonRelease-1>", stop)
ventana.bind("<B1-Motion>", mover) 
ventana.bind("<KeyPress-Escape>", salir)

#* ********** ********** Diseño de la ventana ********** ********** *#
texto_hora = Label(ventana, fg=color_texto, bg='gray', font=('Star Jedi Hollow', 50, 'bold'), width=10)
texto_hora.grid(column=0, row=0, ipadx=1, ipady=1)

texto_fecha12 = Label(ventana, fg=color_texto, bg='gray', font=('Vivaldi', 20, 'bold'))
texto_fecha12.grid(column=0, row=1)

zona_horaria = Label(ventana, fg=color_texto, bg='gray', font=('Lucida Sans', 12))
zona_horaria.grid(column=0, row=2)


obtener_tiempo() #* Activacion de la funcion
ventana.mainloop() #* run ventana

#* Autor: Francisco Velez
