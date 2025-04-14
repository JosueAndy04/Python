from tkinter import (
    Tk,
    Frame,
    Label,
    LabelFrame,
    Checkbutton,
    IntVar,
    Entry,
    StringVar,
    Button,
    Text,
    END,
    filedialog,
    messagebox
)
import random
import datetime


operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comidas[x].get() == 1:
            cuadros_comida[x].config(state="normal")
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state="disabled")
            texto_comida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state="normal")
            if cuadros_bebida[x].get() == 0:
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state="disabled")
            texto_bebida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_postre:
        if variables_postres[x].get() == 1:
            cuadros_postre[x].config(state="normal")
            if cuadros_postre[x].get() == 0:
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state="disabled")
            texto_postre[x].set("0")
        x += 1


def totalfun():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (
            float(cantidad.get()) * precios_comida[p]
        )
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (
            float(cantidad.get()) * precios_bebida[p]
        )
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postres = sub_total_postres + (
            float(cantidad.get()) * precios_postres[p]
        )
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuesto = sub_total * 0.07
    total = sub_total + impuesto

    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postres, 2)}")
    var_costo_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuesto.set(f"$ {round(impuesto, 2)}")
    var_total.set(f"$ {round(total, 2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = (
        f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    )
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, "*" * 58 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, "-" * 104 + "\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_comidas[x]}\t\t{comida.get()}\t$ {round(int(comida.get()) * precios_comida[x], 2)}\n",
            )
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_bebidas[x]}\t\t{bebida.get()}\t$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n",
            )
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_postres[x]}\t\t{postre.get()}\t$ {round(int(postre.get()) * precios_postres[x], 2)}\n",
            )
        x += 1
    
    texto_recibo.insert(END, '-' * 104 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, '-' * 104 + '\n')
    texto_recibo.insert(END, f' Sub-Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, "*" * 58 + "\n")
    texto_recibo.insert(END, 'Gracias')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Recibo guardado con exito')

def resetear():
    texto_recibo.delete(1.0, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    
    for cuadro in cuadros_comida:
        cuadro.config(state='disabled')
    for cuadro in cuadros_bebida:
        cuadro.config(state='disabled')
    for cuadro in cuadros_postre:
        cuadro.config(state='disabled')
    
    for v in variables_comidas:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# iniciar tkinter
aplicacion = Tk()

# size of ventana
aplicacion.geometry("1260x630+0+0")

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fondo
aplicacion.config(bg="burlywood")

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief="flat")

panel_superior.pack(side="top")

# etiqueta titulo
etiqueta_titulo = Label(
    panel_superior,
    text="Sistema de Facturacion",
    fg="azure4",
    font=("Dosis", 58),
    bg="burlywood",
    width=27,
)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief="flat")
panel_izquierdo.pack(side="left")

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief="flat", bg="azure4", padx=80)
panel_costos.pack(side="bottom")

# panel comida
panel_comidas = LabelFrame(
    panel_izquierdo,
    text="Comida",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief="flat",
    fg="azure4",
)
panel_comidas.pack(side="left")

# panel bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo,
    text="Bebidas",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief="flat",
    fg="azure4",
)
panel_bebidas.pack(side="left")

# panel postres
panel_postres = LabelFrame(
    panel_izquierdo,
    text="Postres",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief="flat",
    fg="azure4",
)
panel_postres.pack(side="left")

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief="flat", bg="burlywood")
panel_derecha.pack(side="right")

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_botones.pack()

# lista de productos
lista_comidas = [
    "Pollo",
    "Cordero",
    "Salmon",
    "Merluza",
    "Kebab",
    "Pizza1",
    "Pizza2",
    "Pizza3",
]

lista_bebidas = [
    "Agua",
    "Soda",
    "Jugo",
    "Cola",
    "Vino1",
    "Vino2",
    "Cerveza1",
    "Cerveza2",
]

lista_postres = [
    "Helado",
    "Fruta",
    "Brownies",
    "Flan",
    "Mousse",
    "Pastel1",
    "Pastel2",
    "Pastel3",
]

# generar items
variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # checkbutton
    variables_comidas.append("")
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_comidas[contador],
        command=revisar_check,
    )
    comida.grid(row=contador, column=0, sticky="w")

    # crear cuadors de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(
        panel_comidas,
        font=("Dosis", 16, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_comida[contador],
    )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# generar items
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # checkbutton
    variables_bebidas.append("")
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_bebidas[contador],
        command=revisar_check,
    )
    bebida.grid(row=contador, column=0, sticky="w")

    # crear cuadors de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(
        panel_bebidas,
        font=("Dosis", 16, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_bebida[contador],
    )
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

# generar items
variables_postres = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # checkbutton
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postre = Checkbutton(
        panel_postres,
        text=postre.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=variables_postres[contador],
        command=revisar_check,
    )
    postre.grid(row=contador, column=0, sticky="w")

    # crear cuadors de entrada
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    cuadros_postre[contador] = Entry(
        panel_postres,
        font=("Dosis", 16, "bold"),
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_postre[contador],
    )
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(
    panel_costos,
    text="Costo Comida",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_comida,
)

texto_costo_comida.grid(row=0, column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(
    panel_costos,
    text="Costo Bebida",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_bebida,
)

texto_costo_bebida.grid(row=1, column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(
    panel_costos,
    text="Costo Postre",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_postre,
)

texto_costo_postre.grid(row=2, column=1, padx=41)

# Otras etiquetas
subtotal = Label(
    panel_costos,
    text="Subtotal",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
subtotal.grid(row=0, column=2)

texto_subtotal = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_subtotal,
)

texto_subtotal.grid(row=0, column=3)

# impuesto
impuesto = Label(
    panel_costos,
    text="Impuesto",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
impuesto.grid(row=1, column=2)

texto_impuesto = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_impuesto,
)

texto_impuesto.grid(row=1, column=3, padx=41)

# total
total = Label(
    panel_costos,
    text="Total",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
total.grid(row=2, column=2)

texto_total = Entry(
    panel_costos,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_total,
)

texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ["Total", "Recibo", "Guardar", "Resetear"]
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(
        panel_botones,
        text=boton.title(),
        font=("Dosis", 14, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=9,
    )
    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=totalfun)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(
    panel_recibo,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=58,
    height=10,
)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(
    panel_calculadora,
    font=("Dosis", 16, "bold"),
    width=44,
    bd=1,
)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "*",
    "CE",
    "Borrar",
    "0",
    "/",
]

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=("Dosis", 16, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=8,
    )

    botones_guardados.append(boton)

    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click("7"))
botones_guardados[1].config(command=lambda: click("8"))
botones_guardados[2].config(command=lambda: click("9"))
botones_guardados[3].config(command=lambda: click("+"))
botones_guardados[4].config(command=lambda: click("4"))
botones_guardados[5].config(command=lambda: click("5"))
botones_guardados[6].config(command=lambda: click("6"))
botones_guardados[7].config(command=lambda: click("-"))
botones_guardados[8].config(command=lambda: click("1"))
botones_guardados[9].config(command=lambda: click("2"))
botones_guardados[10].config(command=lambda: click("3"))
botones_guardados[11].config(command=lambda: click("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click("0"))
botones_guardados[15].config(command=lambda: click("/"))


# evitar que la pantalla se cierre
aplicacion.mainloop()
