import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import font
import db



class Login:

    def __init__(self, root):

        self.conet_db = db.Base_datos()

        self.ventana_login = root
        self.ventana_login.title('Login')
        self.ventana_login.resizable(1, 1)
        self.ventana_login.wm_iconbitmap('recursos/icon_martillo.ico')

        self.leffFrame = Label(self.ventana_login, width=200, height=600)
        self.leffFrame.grid(row=0, column=0, padx=10, pady=2)

        self.imagen_Login = tkinter.PhotoImage(file='recursos/Martillo.png')
        Instruct = Label(self.leffFrame, image=self.imagen_Login)
        Instruct.grid(row=0, column=0, padx=20, pady=2)

        self.rightFrame = Label(self.ventana_login, width=200, height=600)
        self.rightFrame.grid(row=0, column=1, padx=10, pady=2)

        self.rightFrame_up = Label(self.rightFrame)
        self.rightFrame_up.grid(row=0, column=0, padx=10, pady=2)

        self.imagen_user = tkinter.PhotoImage(file='recursos/image_user.png')
        Instruct1 = Label(self.rightFrame_up, image= self.imagen_user)
        Instruct1.grid(row=0, column=0, pady=2)

        self.user_frame = LabelFrame(self.rightFrame_up, width=200, height=600)
        self.user_frame.grid(row=1, column=0, padx=10, pady=2)

        self.etiqueta_nombre = Label(self.user_frame, text='   Usuario:*   ', font=('Calibri', 13), background='#68AFFF')
        self.etiqueta_nombre.grid(row=0, column=0, columnspa=1)

        self.input_user = Entry(self.user_frame, font=('Calibri', 13))
        self.input_user.grid(row=0, column=1)
        self.input_user.focus()



        self.password_frame = LabelFrame( self.rightFrame_up, width=200, height=600)
        self.password_frame.grid(row=2, column=0, padx=10, pady=2)

        self.etiqueta_password = Label(self.password_frame, text='Contraseña:*', font=('Calibri', 13), background='#68AFFF')
        self.etiqueta_password.grid(row=0, column=0, columnspa=1)

        self.input_password = Entry(self.password_frame, font=('Calibri', 13))
        self.input_password.grid(row=0, column=1)

        self.frame_boton = Label(self.rightFrame_up)
        self.frame_boton.grid(row=3, column=0)

        self.boton_acceder = ttk.Button(self.frame_boton, text="Acceder", command=self.comprobar_usuario_password, style='my.TButton')
        self.boton_acceder.grid(row=0, column=0, padx=10, pady=2)

        self.boton_registrar = ttk.Button(self.frame_boton, text="Registrarse", command=self.registrar_nuevo_usuario,style='my.TButton')
        self.boton_registrar.grid(row=0, column=1, padx=10, pady=2)

        self.mensaje = Label(text="", fg = 'red')
        self.mensaje.grid(row=3, column= 0, columnspan =2 , sticky = W +E)

        self.id_usuario = ''
        self.sesion_iniciada = False

        self.tipo_usuario = ''


    def consultar_id_usuario_contrasena_vendedor(self, nombre,password):  # el id_producto viene por defecto cuando inicia el comprador y ve sus productos
        query = "SELECT id, nombre, password FROM vendedor WHERE nombre = '{}' AND password = '{}'".format(nombre, password)
        self.id_usuario = self.conet_db.db_consulata(query)
        return self.id_usuario.fetchone()

    def consultar_id_usuario_contrasena_comprador(self, nombre,password):  # el id_producto viene por defecto cuando inicia el comprador y ve sus productos
        query = "SELECT id, nombre, password FROM comprador WHERE nombre = '{}' AND password = '{}'".format(nombre, password)
        self.id_usuario = self.conet_db.db_consulata(query)
        return self.id_usuario.fetchone()


    def consultar_id_usuario_contrasena(self, nombre,password):
        self.id_comprador = self.consultar_id_usuario_contrasena_comprador(nombre,password)
        if self.id_comprador is not None:
            self.tipo_usuario = 'Comprador'
            return self.id_comprador

        self.id_vendedor = self.consultar_id_usuario_contrasena_vendedor(nombre,password)
        if self.id_vendedor is not None:
            self.tipo_usuario = 'Vendedor'
            return self.id_vendedor




    def comprobar_usuario_password(self):
        try:

            self.datos_ingresados = self.consultar_id_usuario_contrasena(self.input_user.get(), self.input_password.get())

            self.identificador = self.datos_ingresados[0]
            self.nombre_db = self.datos_ingresados[1]
            self.password_db = self.datos_ingresados[2]
            self.id_usuario = self.identificador
            self.sesion()
            self.ventana_login.destroy()

        except TypeError:
            self.mensaje['text'] = 'Contraseña o usuario incorrectos'


    def sesion(self):
        if self.sesion_iniciada == True:
            self.sesion_iniciada = False
        else:
            self.sesion_iniciada = True
        return self.sesion_iniciada





    def registrar_nuevo_usuario(self):

        self.rightFrame_down = Label(self.rightFrame, width=200, height=600)
        self.rightFrame_down.grid(row=1, column=0, padx=10, pady=2)

        self.user_frame_registro = LabelFrame( self.rightFrame_down, width=200, height=600)
        self.user_frame_registro.grid(row=0, column=0, padx=10, pady=2)

        self.etiqueta_nombre_registro = Label(self.user_frame_registro, text=' Nombre completo:* ', font=('Calibri', 13), background='#F38276')
        self.etiqueta_nombre_registro.grid(row=0, column=0, columnspa=1)

        self.input_user_registro = Entry(self.user_frame_registro, font=('Calibri', 13))
        self.input_user_registro.grid(row=0, column=1)
        self.input_user_registro.focus()


        self.password_frame_registro = LabelFrame(self.rightFrame_down, width=200, height=600)
        self.password_frame_registro.grid(row=1, column=0, padx=10, pady=2)

        self.etiqueta_password_nuevo = Label(self.password_frame_registro, text=' Definir contraseña:*', font=('Calibri', 13), background='#F38276')
        self.etiqueta_password_nuevo.grid(row=0, column=0, columnspa=1)

        self.input_password_nuevo = Entry(self.password_frame_registro, font=('Calibri', 13))
        self.input_password_nuevo.grid(row=0, column=1)

        self.password_frame_registro_repetir = LabelFrame(self.rightFrame_down, width=200, height=600)
        self.password_frame_registro_repetir.grid(row=2, column=0, padx=10, pady=2)

        self.etiqueta_password_repetir = Label(self.password_frame_registro_repetir, text=' Repetir contraseña:*', font=('Calibri', 13), background='#F38276')
        self.etiqueta_password_repetir.grid(row=0, column=0, columnspa=1)

        self.input_password_repetir = Entry(self.password_frame_registro_repetir, font=('Calibri', 13))
        self.input_password_repetir.grid(row=0, column=1)

        self.frame_tipo_usuario = LabelFrame(self.rightFrame_down, width=200, height=600)
        self.frame_tipo_usuario.grid(row=3, column=0, padx=10, pady=2)


        self.desplegable_tipo_usuario = Label(self.frame_tipo_usuario, text=' Empresa/particular:*', font=('Calibri', 13),  background='#F3D683')
        self.desplegable_tipo_usuario.grid(row=0,  column=0)
        self.input_desplegable_tipo = ttk.Combobox(self.frame_tipo_usuario, width=2,
        values = ['Empresa', 'Particular'])
        self.input_desplegable_tipo.set('Empresa')
        self.input_desplegable_tipo.grid(row=0, column=1, padx=16, pady=2)
        self.input_desplegable_tipo.config(width=20)

        self.frame_checkbox = Label(self.rightFrame_down, width=200, height=600)
        self.frame_checkbox.grid(row=4, column=0, padx=10, pady=2)


        self.checkbox_var1 = IntVar()
        self.checkbox_var2 = IntVar()

        self.checkbox1 = Checkbutton(self.frame_checkbox, text="Vender", variable=self.checkbox_var1, command=lambda: self.checkbox_var2.set(0))
        self.checkbox1.grid(row=0, column=0, padx=10, pady=2)

        self.checkbox2 = Checkbutton(self.frame_checkbox, text="Comprar", variable=self.checkbox_var2, command=lambda: self.checkbox_var1.set(0))
        self.checkbox2.grid(row=0, column=1, padx=10, pady=2)

        self.frame_boton_registro = Label(self.rightFrame_down, width=200, height=600)
        self.frame_boton_registro.grid(row=5, column=0, padx=10, pady=2)

        self.boton_acceder = ttk.Button(self.frame_boton_registro, text="Registrar ahora", command=self.registrar_usuario,style='my.TButton')
        self.boton_acceder.grid(row=0, column=0 , padx=100, pady=2)


    def registrar_usuario(self):
        self.checkbox1_state = self.checkbox_var1.get()
        self.checkbox2_state = self.checkbox_var2.get()

        if self.checkbox1_state == 1 and  self.checkbox2_state == 0:
            self.nombre_empresa = self.input_user_registro.get()
            self.registro_contrasena = self.input_password_nuevo.get()
            self.registro_contrasena_repetir = self.input_password_repetir.get()
            if self.registro_contrasena == self.registro_contrasena_repetir:
                parametros = (self.nombre_empresa, self.registro_contrasena)
                query = 'INSERT INTO vendedor VALUES(NULL, ?, ?)'
                self.conet_db.db_consulata(query, parametros)
                messagebox.showinfo(message="Se ha registrado correctamente. Introduzca los datos", title="Título")
                self.sesion()
                self.ventana_login.destroy()
                #self.sesion()


            else:
                self.mensaje['text'] = 'Las contraseñas no coinciden'


        if self.checkbox1_state == 0 and  self.checkbox2_state == 1:
            self.nombre_comprador = self.input_user_registro.get()
            self.registro_contrasena_comprador = self.input_password_nuevo.get()
            self.registro_contrasena_comprador_repetir = self.input_password_repetir.get()
            self.comprador_empresa = 1 if self.input_desplegable_tipo.get() == 'Empresa' else 0

            if self.registro_contrasena_comprador == self.registro_contrasena_comprador_repetir:
                parametros = (self.nombre_comprador, self.comprador_empresa, self.registro_contrasena_comprador)
                query = 'INSERT INTO comprador VALUES(NULL,?, ?, ?)'
                self.conet_db.db_consulata(query, parametros)
                messagebox.showinfo(message="Se ha registrado correctamente. Introduzca los datos", title="Título")
                self.sesion()
                self.ventana_login.destroy()


            else:
                self.mensaje['text'] = 'Las contraseñas con coinciden'

class Comprador:


    def __init__(self, root, user):
        self.ventana = root
        self.conet_db = db.Base_datos()

        self.ventana.title('TechAuction')
        self.ventana.resizable(1, 1)
        self.ventana.wm_iconbitmap('recursos/icon_martillo.ico')
        self.mensaje = Label(text="", fg = 'red')
        self.mensaje.grid(row=4, column= 0, columnspan =2 , sticky = W +E)
        self.usuario = user


        self.frame_barra_busqueda = Frame(self.ventana)
        self.frame_barra_busqueda.grid(row=0, column=0, padx=10, pady=2)

        self.eitiqueta_buscador = Label(self.frame_barra_busqueda, text= 'Buscar', font=('Calibri', 13))
        self.eitiqueta_buscador.grid(row=0, column=0, columnspa=1)

        self.input_busqueda = Entry(self.frame_barra_busqueda, font=('Calibri', 13))
        self.input_busqueda.grid(row=0, column=1)
        self.input_busqueda.focus()

        lupa_icon = PhotoImage(file="recursos/icon_lupa.png")
        self.boton_buscar = ttk.Button(self.frame_barra_busqueda, image=lupa_icon, command=self.tabla_productos,
                                       width=40,style='my.TButton')
        self.boton_buscar.grid(row=0,rowspan = 1, column =2, padx=10, pady=2)
        self.boton_buscar.image = lupa_icon

        self.eitiqueta_categoria = Label(self.frame_barra_busqueda, text='Buscar por categoría', font=('Calibri', 13))
        self.eitiqueta_categoria.grid(row=1, column=0, columnspa=1)

        self.input_desplegable = ttk.Combobox(self.frame_barra_busqueda, width=17,
        values=['Calculadora', 'Ebook', 'Ordenador portátil',
      'Altavoz inteligente', 'Webcam', 'Monitor',
      'Teléfono móvil', 'Tableta', 'Reloj inteligente',
      'Reproductor de streaming de contenidos',
      'Auriculares inalámbricos', 'Televisor', 'Tableta plegable',
      'Pulsera de actividad', 'Cámara de seguridad',
      'Consola de videojuegos', 'Reloj de pulsera', 'Cámara de acción',
      'Sintetizador',
      'Timbre inteligente con cámara de seguridad', 'Microondas'])
        self.input_desplegable.set('Seleccionar')
        self.input_desplegable.grid(row=1, column=1)

        self.boton_hist_ofertas = ttk.Button(self.ventana, text="Hacer una oferta", command=self.hacer_una_puja,style='my.TButton')
        self.boton_hist_ofertas.grid(row=2, column=0, padx=10, pady=2)


        self.finalizar = ttk.Button(self.frame_barra_busqueda, text="Cerrar sesion", command=self.finalizar,style='my.TButton')
        self.finalizar.grid(row=0, column=3, padx=10, pady=2)

        self.frame_tabla = Label(self.ventana, text='Productos', width=200, height=200)
        self.frame_tabla.grid(row=1, column=0, padx=10, pady=2)

        self.tabla = ttk.Treeview(self.frame_tabla, height=10, columns=('#0', '#1', '#2'), style='mystyle.Treeview')

        self.imagen = tkinter.PhotoImage(file='recursos/Logo_comprador.png')
        frame_imagen = Label(self.frame_tabla, image=self.imagen)
        frame_imagen.grid(row=1, column=0, padx=20, pady=2)

        self.estado_mi_ofertas()

    def crear_tabla(self, columnas = (), valores = (), nombre_tabla = None):

        self.frame_tabla = LabelFrame(self.ventana,text = nombre_tabla, width=200, height=200)
        self.frame_tabla.grid(row=1, column=0, padx=10, pady=2)

        style = ttk.Style()
        style.configure("bold_header.Treeview.Heading", font=("Arial", 9, "bold"))

        self.tabla = ttk.Treeview(self.frame_tabla, height = 10, columns =  ('#0', '#1', '#2'), style = "bold_header.Treeview")
        self.tabla.grid(row = 0, column = 0, columnspan = 1)

        self.scrollbar = ttk.Scrollbar(self.frame_tabla, orient='vertical', command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        font_bold = font.Font(family='Arial', size=12, weight='bold')
        self.tabla.heading('#0', text= columnas[0], anchor = CENTER)
        self.tabla.heading('#1', text= columnas[1], anchor = CENTER)
        self.tabla.heading('#2', text= columnas[2], anchor=CENTER)
        self.tabla.heading('#3', text= columnas[3], anchor=CENTER)


        #self.tabla.column('#0', anchor='center', width=100)
        self.tabla.column('#1', anchor='center', width=100)
        self.tabla.column('#2', anchor='center', width=100)
        self.tabla.column('#3', anchor='center', width=100)


        for fila in valores:
            self.tabla.insert('', 0, text=fila[1], values=(fila[2], fila[2]))

    def tabla_productos(self):

        try:
            self.crear_tabla(columnas = ('NOMBRE', 'PRECIO SALIDA','PUJA MÁS ALTA', 'VENDEDOR' ), nombre_tabla = 'Productos')
        except IndexError:
            print('Tabla vacia')

        if len(self.input_busqueda.get()) == 0:
            self.busqueda = self.input_desplegable.get()
            productos = self.ver_productos_por_categor(self.busqueda)



        else:
            self.busqueda = self.input_busqueda.get()
            productos = self.ver_productos(str(self.busqueda))

        for fila in productos:

            try:
                precio_maximo = max(self.precios_ofertados(fila[0]))[0]

            except:
                precio_maximo = 0
            self.tabla.insert('', 0, text=fila[1], values=(fila[2], precio_maximo, fila[5] ))


    def ver_productos(self, nombre):
        query = '''SELECT a.id, a.nombre, a.precio, a.tipo, a.id_vendedor, b.nombre
                    FROM producto a
                    INNER JOIN vendedor b
                    ON a.id_vendedor = b.id
                    WHERE a.nombre LIKE "%{}%" and a.disponible = 1'''.format(nombre)
        articulos = self.conet_db.db_consulata(query)
        return articulos

    def ver_productos_por_categor(self, categoria):
        query = '''SELECT a.id, a.nombre, a.precio, a.tipo, a.id_vendedor, b.nombre
                      FROM producto a
                      INNER JOIN vendedor b
                      ON a.id_vendedor = b.id
                      WHERE a.tipo = "{}" and a.disponible = 1'''.format(categoria)
        articulos_por_categoria = self.conet_db.db_consulata(query)
        return articulos_por_categoria



    def precios_ofertados(self, id_producto):
        query = 'SELECT precio_ofertado FROM demanda WHERE id_producto = {}'.format(id_producto)
        precios = self.conet_db.db_consulata(query)
        return precios

    def hacer_una_puja(self):


        try:
            seleccion_producto = self.tabla.item(self.tabla.selection())
            item = seleccion_producto['text']
            vendedor = seleccion_producto['values'][2]

        except IndexError:
            messagebox.showwarning(message='No se ha seleccionado el producto')
            return

        query = '''SELECT a.id, a.nombre, a.precio, b.id, b.nombre
                    FROM producto a 
                    INNER JOIN vendedor b
                    WHERE a.nombre = '{}' and b.nombre  =  '{}' '''.format(item, vendedor)
        consulta = self.conet_db.db_consulata(query)
        consulta = consulta.fetchall()


        try:
            precio_maximo = max(self.precios_ofertados(consulta[0][0]))[0]

        except:
            precio_maximo = 0
        id_producto = consulta[0][0]
        nombre_producto = consulta[0][1]
        precio_salida = consulta[0][2]
        id_vendedor = consulta[0][3]
        puja_mas_alta = precio_maximo

        self.ventana_pujar = Toplevel()
        self.ventana_pujar.title = 'Ofertar precio'
        self.ventana_pujar.resizable(1,1)
        self.ventana_pujar.wm_iconbitmap('recursos/icon_martillo.ico')


        titulo = Label(self.ventana_pujar)
        titulo.grid(column=0, row=0)

        frame_ep = Label(self.ventana_pujar, font=('Calibri', 16, 'bold'))
        frame_ep.grid(row = 1, column = 0, columnspan = 10, pady = 20)

        self.etiqueta_nombre = Label(frame_ep, text = 'Producto: ', font=('Calibri', 13))
        self.etiqueta_nombre.grid(row = 2, column = 0)
        self.input_nombre_anterior = Entry(frame_ep, textvariable = StringVar(self.ventana_pujar, value = nombre_producto), state = 'readonly', font=('Calibri', 13))
        self.input_nombre_anterior.grid(row = 2, column = 1)

        self.etiqueta_precio_salida = Label(frame_ep, text='Precio salida: ', font=('Calibri', 13))
        self.etiqueta_precio_salida.grid(row=3, column=0)
        self.input_precio_salida = Entry(frame_ep, textvariable=StringVar(self.ventana_pujar, value = precio_salida), state='readonly', font=('Calibri', 13))
        self.input_precio_salida.grid(row = 3, column = 1)

        self.etiqueta_puja_mas_alta = Label(frame_ep, text='Puja más alta:', font=('Calibri', 13))
        self.etiqueta_puja_mas_alta.grid(row = 5, column = 0)
        self.input_puja_mas_alta = Entry(frame_ep, textvariable=StringVar(self.ventana_pujar, value = puja_mas_alta),
                                           state='readonly', font=('Calibri', 13))
        self.input_puja_mas_alta.grid(row = 5, column=1)

        self.etiqueta_determinar_precio = Label(frame_ep, text='Determinar precio: ', font=('Calibri', 13))
        self.etiqueta_determinar_precio.grid(row = 6, column=0)

        self.input_precio_ofertado = Entry(frame_ep, font=('Calibri', 13))
        self.input_precio_ofertado.grid(row = 6, column=1)
        self.input_precio_ofertado.focus()


        self.boton_guardar_precio= ttk.Button(frame_ep, text = 'Guardar precio', style='my.TButton', command = lambda:
            self.registrar_demanda(id_producto, self.input_precio_ofertado.get(),self.usuario, id_vendedor))
        self.boton_guardar_precio.grid(row = 7, columnspan = 2, sticky = W + E)



    def registrar_demanda(self, id_producto, precio_ofertado,id_comprador, id_vendedor):

        if len(precio_ofertado) == 0:
            continuar_sin_precio = messagebox.askretrycancel(message="No se ha introducido ningún precio")
            if continuar_sin_precio == False:
                self.ventana_pujar.destroy()
        else:

            try:
                precio_ofertado = float(precio_ofertado)
                parametros = (id_producto, precio_ofertado, id_comprador, id_vendedor, 0)
                query = 'INSERT INTO demanda VALUES(NULL, ?, ?, ?, ?, ?)'
                self.conet_db.db_consulata(query, parametros)
                messagebox.showinfo(message="El precio se ha registrado correctamente")
                cuestion = messagebox.askquestion(message = '¿Desea ofertar un nuevo precio?')
                if cuestion == 'no':
                    self.ventana_pujar.destroy()


            except ValueError:
                continuar = messagebox.askretrycancel(message="El precio introducido es incorrecto")
                if continuar == False:
                    self.ventana_pujar.destroy()

    def mis_ofertas(self):
        query = '''SELECT id, estado
                  FROM demanda 
                  WHERE id_comprador = {} '''.format(self.usuario)
        consult_estado = self.conet_db.db_consulata(query)
        consult_estado = consult_estado.fetchall()
        return consult_estado

    def estado_mi_ofertas(self):
        #

        mis_ofertas = self.mis_ofertas()
        for estado in mis_ofertas:
            if estado[1] == 1:
                query = '''SELECT a.nombre, b.precio_ofertado
                        FROM producto a 
                        INNER JOIN demanda b
                        ON a.id = b.id_producto
                        WHERE  b.estado = 1 AND b.id = {} AND b.id_comprador = {} '''.format(estado[0], self.usuario)
                consult_ofertas_aceptas = self.conet_db.db_consulata(query)
                consult_ofertas_aceptas = consult_ofertas_aceptas.fetchall()[0]
                nombre_producto = consult_ofertas_aceptas[0]
                precio_producto =  consult_ofertas_aceptas[1]
                notificacion = 'Su oferta de {} euros por {} ha sido  aceptada'.format(precio_producto, nombre_producto)
                messagebox.showinfo(message=notificacion)

    def finalizar(self):
        self.ventana.destroy()

class Vendedor:


    def __init__(self, root, user):
        self.conet_db = db.Base_datos()

        self.ventana = root
        self.ventana.title('TechAuction')
        self.ventana.resizable(1, 1)
        self.ventana.wm_iconbitmap('recursos/icon_martillo.ico')

        self.usuario = user

        self.frama_titulo = Frame(self.ventana, width=200, height=200)
        self.frama_titulo.grid(row=0, padx=10, pady=2)

        self.imagen = tkinter.PhotoImage(file='recursos/Auction.png')
        self.imagen2 = tkinter.PhotoImage(file='recursos/Logo.png')
        self.Instruct = Label(self.frama_titulo, image= self.imagen)
        self. Instruct.grid(row=0, column=1, padx=20, pady=2)
        self.Instruct2 = Label(self.frama_titulo, image=self.imagen)
        self.Instruct2.grid(row=0, column=3, padx=20, pady=2)
        self.Instruct3 = Label(self.frama_titulo, image=self.imagen2)
        self.Instruct3.grid(row=0, column=2, padx=20, pady=2)


        self.downFrame = LabelFrame(self.ventana, text='Mis productos', font=('Calibri', 13))
        self. downFrame.grid(row = 1, column = 0, pady=20)

        self.tabla = ttk.Treeview(self.downFrame, height = 10, columns =  ('#0', '#1'), style = 'mystyle.Treeview')
        self.tabla.grid(row = 1, column = 0, columnspan = 3)

        self.tabla.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tabla.heading('#1', text='Precio de salida', anchor = CENTER)
        self.tabla.heading('#2', text='Puja más alta', anchor=CENTER)

        self.mensaje = Label(text="", fg = 'red')
        self.mensaje.grid(row=4, column= 0, columnspan =2 , sticky = W +E)

        self.get_productos()





        self.frame_botones = Label(self.ventana, width=200, height=600)
        self.frame_botones.grid(row=2, column=0, padx=10, pady=2)

        self.boton_sesion = ttk.Button(self.frame_botones, text="Cerrar sesion", command=self.finalizar,style='my.TButton' )
        self.boton_sesion.grid(row=0, column=0, padx=10, pady=2)

        self.boton_similares = ttk.Button(self.frame_botones, text=" Ver productos similares", command=self.tabla_productos_similares,
                                          style='my.TButton')
        self.boton_similares.grid(row=0, column=1, padx=10, pady=2)

        self.boton_historial = ttk.Button(self.frame_botones, text="Historial de ofertas", command=self.tabla_historial_ofertas,
                                          style='my.TButton')
        self.boton_historial.grid(row=0, column=2, padx=10, pady=2)

        self.boton_registro = ttk.Button(self.frame_botones, text="Registrar nuevo producto", command=self.registrar_producto
                                         ,style='my.TButton')
        self.boton_registro.grid(row=0, column=3, padx=10, pady=2)

        self.boton_actualizar = ttk.Button(self.frame_botones, text="Actualizar", command=self.get_productos,style='my.TButton')
        self.boton_actualizar.grid(row=0, column=4, padx=10, pady=2)





    def crear_tabla(self, columnas = (), valores = (), nombre_tabla = None):

        self.frame_tabla2 = LabelFrame(self.ventana, text= nombre_tabla, font=('Calibri', 13))
        self.frame_tabla2.grid(row = 3, column = 0, columnspa = 8, pady=20)

        self.tabla2 = ttk.Treeview(self.frame_tabla2, height = 10, columns =  ('#0', '#1'), style = 'mystyle.Treeview')
        self.tabla2.grid(row = 2, column = 0, columnspan = 1)

        self.tabla2.heading('#0', text = columnas[0], anchor = CENTER)
        self.tabla2.heading('#1', text= columnas[1], anchor = CENTER)
        self.tabla2.heading('#2', text= columnas[2], anchor=CENTER)
        for fila in valores:
            self.tabla2.insert('', 0, text=fila[0], values=(fila[1], fila[2]))


    def mis_productos(self):

        query = 'SELECT id, nombre, precio FROM producto WHERE id_vendedor = {} and disponible = 1'.format(self.usuario)
        articulos = self.conet_db.db_consulata(query)
        return articulos

    def precios_ofertados(self, id_producto):
        query = 'SELECT precio_ofertado FROM demanda WHERE id_producto = {}'.format(id_producto)
        precios = self.conet_db.db_consulata(query)
        return precios

    def consultar_oferta_comprador(self):

        self.mensaje['text'] = ''
        try:
            nombre = self.tabla.item(self.tabla.selection())['text']

            query = '''SELECT id
                    FROM producto
                    WHERE nombre = '{}' AND id_vendedor = {}'''.format(nombre, self.usuario)  # 17: id_vendedor
            id_producto = self.conet_db.db_consulata(query)

            if id_producto:
                id_producto = list(id_producto)[0][0]
            else:
                return

        except IndexError as e:
            return


        query = '''SELECT a.precio_ofertado, b.nombre, b.empresa
                FROM demanda a 
                INNER JOIN comprador b
                ON a.id_comprador = b.id
                WHERE a.id_producto = {}'''.format(id_producto)
        oferta = self.conet_db.db_consulata(query)
        return oferta

    def consulta_produtos_similares(self):

        try:
            nombre_producto = self.tabla.item(self.tabla.selection())['text']
            self.ver_categoria(nombre_producto)

        except IndexError as e1:
            messagebox.showwarning(message= 'No se ha seleccionado el producto')
            return

        tipo_producto = self.ver_categoria(nombre_producto)

        query = '''SELECT tipo, nombre, precio
                    FROM producto
                    WHERE tipo = '{}' and  id_vendedor <> {} '''.format(tipo_producto, self.usuario)
        similares = self.conet_db.db_consulata(query)
        return similares

    def get_productos(self):

        registros_tabla = self.tabla.get_children()
        for fila in registros_tabla:
            self.tabla.delete(fila)


        registros_db = self.mis_productos()

        for fila in registros_db:

            try:
                precio_maximo = max(self.precios_ofertados(fila[0]))[0]

            except:
                precio_maximo = 0

            self.tabla.insert('', 0, text=fila[1], values=(fila[2], precio_maximo))  # parámetros:

    def consult_demanda(self):

        query = '''SELECT producto.nombre, demanda.precio_ofertado, comprador.nombre
        FROM producto, demanda, comprador
        WHERE demanda.id_comprador = comprador.id and demanda.id_producto = producto.id'''
        demanda = self.conet_db.db_consulata(query)
        return demanda

    def tabla_historial_ofertas(self):

        consulta = self.consultar_oferta_comprador()
        if consulta is not None:
            self.crear_tabla(('Ofertas', 'Comprador', 'Empresa'), consulta, 'Historial de ofertas')
            self.boton_ofertas = ttk.Button(self.ventana, text="Vender", command=self.vender, width=20,style='my.TButton')
            self.boton_ofertas.grid(row=4, column = 0 , padx=10, pady=2)
        else:
            messagebox.showwarning(message='No se ha seleccionado el producto')
            return

        consulta = self.consultar_oferta_comprador()
        self.crear_tabla(('Ofertas', 'Comprador', 'Empresa'), consulta, 'Historial de ofertas')

    def tabla_productos_similares(self):
        productos = self.consulta_produtos_similares()

        try:
            if productos is not None:
                self.crear_tabla(('Tipo', 'Nombre', 'Precio'), productos, 'Productos similares')


        except TypeError as e:
            messagebox.showwarning(message='No se ha seleccionado el producto')
            return

    def registrar_producto(self):

        self.ventana_nuevo_producto = Toplevel()
        self.ventana_nuevo_producto.wm_iconbitmap('recursos/icon_martillo.ico')
        self.ventana_nuevo_producto.title = 'Registrar producto nuevo'
        self.ventana_nuevo_producto.resizable(1, 1)

        upFrame = LabelFrame(self.ventana_nuevo_producto, text='Nuevo producto', width=200, height=600)
        upFrame.grid(row=0, column=0, padx=10, pady=2)

        self.etiqueta_nombre = Label(upFrame, text='Nombre:', font=('Calibri', 13))
        self.etiqueta_nombre.grid(row=0, column=0, columnspa=1)

        self.input_nombre = Entry(upFrame, font=('Calibri', 13))
        self.input_nombre.grid(row=0, column=1)

        self.etiqueta_categoria = Label(upFrame, text='Categoría:', font=('Calibri', 13))
        self.etiqueta_categoria.grid(row=0, column=2, columnspa=1)
        self.input_desplegable = ttk.Combobox(upFrame, width=17,
        values = ['Calculadora', 'Ebook', 'Ordenador portátil', 'Altavoz inteligente', 'Webcam', 'Monitor',
         'Teléfono móvil', 'Tableta', 'Reloj inteligente', 'Reproductor de streaming de contenidos',
         'Auriculares inalámbricos', 'Televisor', 'Tableta plegable', 'Pulsera de actividad', 'Cámara de seguridad',
         'Consola de videojuegos', 'Reloj de pulsera', 'Cámara de acción', 'Sintetizador',
         'Timbre inteligente con cámara de seguridad', 'Microondas'])
        self.input_desplegable.set('Ordenador portátil')
        self.input_desplegable.grid(row=0, column=3)


        downFrame = LabelFrame(self.ventana_nuevo_producto, text='Elegir precio', width=200, height=600)
        downFrame.grid(row=1, column=0, padx=10, pady=2)

        self.etiqueta_precio = Label(downFrame, text='Precio:', font=('Calibri', 13))
        self.etiqueta_precio.grid(row=0, column=0, columnspa=1)
        self.input_precio = Entry(downFrame, font=('Calibri', 13))
        self.input_precio.grid(row=0 , column=1)

        # self.recomend_precio = ttk.Button(downFrame, text='Recomendar precio')
        # self.recomend_precio.grid(row=0, column=2, columnspa=2)

        frame_guardar = Label(self.ventana_nuevo_producto, width=200, height=600)
        frame_guardar.grid(row=2, column=0, padx=10, pady=3)

        self.guardar = ttk.Button(frame_guardar,style='my.TButton', text='Guardar producto', command = lambda:
                              self.registrar_productos(self.input_nombre.get(),
                                                            self.input_precio.get(),
                                                            self.input_desplegable.get(),
                                                            ))
        self.guardar.grid(row=0, column=0, columnspa=2)

    def registrar_productos(self, nombre, precio, tipo):
        parametros = (nombre, precio, self.usuario, tipo, 1)
        query = 'INSERT INTO producto VALUES(NULL, ?, ?, ?, ?, ?)'
        self.conet_db.db_consulata(query, parametros)
        cuestion = messagebox.askquestion(message='El producto se ha registrado correctamente. ¿Desea registrar un nuevo producto?')
        if cuestion == 'no':
            self.ventana_nuevo_producto.destroy()

    def ver_categoria(self, nombre_producto):
        query = 'SELECT tipo, nombre FROM producto WHERE nombre = "{}"'.format(nombre_producto)
        articulos = self.conet_db.db_consulata(query)
        categoria = list(dict(articulos).keys())[0]
        return categoria

    def obtener_id_comprador(self, nombre_comprador):
        query = 'SELECT id FROM comprador WHERE nombre = "{}"'.format(nombre_comprador)
        consult_id_demandante = self.conet_db.db_consulata(query)
        id = consult_id_demandante.fetchone()[0]
        return id


    def obtener_id_producto(self, id_comprador, precio_ofertado):
        query = '''SELECT id_producto
                 FROM demanda
                 WHERE id_comprador = {} and precio_ofertado = {} '''.format(id_comprador, precio_ofertado)
        consult_id_producto = self.conet_db.db_consulata(query)
        id_producto = consult_id_producto.fetchone()[0]
        return id_producto

    def obtener_nombre_producto(self, id_producto):
        query = '''SELECT nombre
                 FROM producto
                 WHERE id = {}  '''.format(id_producto)
        consult_nombre_producto = self.conet_db.db_consulata(query)
        nombre_producto = consult_nombre_producto.fetchone()[0]
        return nombre_producto

    def actualizar_estado_producto(self, id_producto):
        query = '''UPDATE producto
                    SET disponible = 0
                    WHERE id = {} '''.format(id_producto)
        self.conet_db.db_consulata(query)


    def vender(self):
        self.mensaje['text'] = ''
        try:
            demanda = self.tabla2.item(self.tabla2.selection())
            self.precio_ofertado = demanda['text']
            self.nombre_comprador = demanda['values'][0]

            self.id_comprador = self.obtener_id_comprador(self.nombre_comprador)
            self.id_producto = self.obtener_id_producto(self.id_comprador, self.precio_ofertado)
            self.nombre_producto = self.obtener_nombre_producto(self.id_producto)

            self.actualizar_estado_producto(self.id_producto)

            mensaje_venta = 'Se ha efectuado la venta de {} a {} por valor de {} euros'.format(self.nombre_producto,
                                                                                               self.nombre_comprador,
                                                                                               self.precio_ofertado)
            messagebox.showinfo(message=mensaje_venta)
            query = '''UPDATE demanda
                        SET  estado = 1
                        WHERE id_comprador = {}  and id_producto = {}'''.format(self.id_comprador, self.id_producto)
            self.conet_db.db_consulata(query)


        except IndexError:
            messagebox.showwarning(message='No ha seleccionado la oferta o actualmente no hay ninguna oferta por el producto que está intentando vender')

        except Exception as e:
            messagebox.showwarning(message = 'Esta opción solo está dispinible en la tabla "Historial de ofertas"')


    def finalizar(self):
        self.ventana.destroy()


