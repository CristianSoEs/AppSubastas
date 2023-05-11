from tkinter import *
import db
from models import Login
from models import Vendedor
from models import Comprador


if __name__ == '__main__':
    while True:
        root = Tk()
        app = Login(root)
        root.mainloop()
        id_usuario =  app.id_usuario
        if app.sesion_iniciada == False:
            break


        if app.sesion_iniciada == True and app.tipo_usuario == 'Vendedor':
            root = Tk()
            app2 = Vendedor(root, id_usuario)
            root.mainloop()
        if app.sesion_iniciada  == True and app.tipo_usuario == 'Comprador':
            root = Tk()
            app3 = Comprador(root,id_usuario)
            root.mainloop()



