# importacion de librerias
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import preguntas
# iniciacion de variables
ques =1
puntaje=0

# funcion encargada de la seleccion de las preguntas y respuestas a mostrar
def select():

       # preguntaSelecionada, respuestaseleccionada = preguntas.generador_preguntas()
        global i, respu_usuario, l1, r1, r2, r3, r4, ques,puntaje
        x = i.get()
        i.set(-1)
        print(x)
        if x==1:

            if ques <5:
                l1["text"]= preguntaSelecionada[ques]
                print(ques)

                r1["text"] = respuestaseleccionada[ques][0][0]
                r1['value']= respuestaseleccionada[ques][0][1]
                r2["text"] = respuestaseleccionada[ques][1][0]
                r2['value'] = respuestaseleccionada[ques][1][1]
                r3["text"] = respuestaseleccionada[ques][2][0]
                r3['value'] = respuestaseleccionada[ques][2][1]
                r4["text"] = respuestaseleccionada[ques][3][0]
                r4['value'] = respuestaseleccionada[ques][3][1]


                puntaje=(puntaje*2)+(100)

                label = Label(ventana, text="Su puntuación es ", font='verdana 18 bold', justify='center')
                label.place(x=100, y=350)
                label1 = Label(ventana, text=puntaje, font='verdana 15 bold', justify='center')
                label1.place(x=350, y=355)
                lnivel = Label(ventana, text='nivel', font=("cambria", 20, "bold"))
                lnivel.place(x=0, y=20)
                lnivel2 = Label(ventana, text=ques+1, font=("cambria", 20, "bold"))
                lnivel2.place(x=80, y=20)


            elif ques==5:

                puntajefinal=str(5000)
                cursor.execute("update quiz set `puntaje`='" + puntajefinal + "' where `nombre`='" + uname + "'")
                cursor.execute("commit")
                messagebox.showinfo("FIN", "FELICIDADES HA GANADO 5000")


                ventana.destroy()

        else:
            #si el jugador tiene la respuesta errada sale del juego y su puntaje =0
            messagebox.showinfo("FIN", "Ha perdido su puntaje es 0")
            cursor.execute("update quiz set `puntaje`='0' where `nombre`='"+uname+"'")
            cursor.execute("commit")

            ventana.destroy()


        ques = ques + 1

#funcion encargada de almacenar y mostrar el puntaje cuando el jugador sale voluntariamente del juego
def puntaje_acumulado():
    puntajefinal=str(puntaje)
    labelfinal = Label(ventana, text="FIN DEL JUEGO SU PUNTUACION ES DE:", font=("cambria", 18))
    labelfinal.place(x=10, y=350)
    labelfinal1 = Label(ventana, text=puntaje, font=("cambria", 18, "bold"))
    labelfinal1.place(x=450, y=350)

    cursor.execute("update quiz set `puntaje`='"+puntajefinal+"' where `nombre`='"+uname+"'")
    cursor.execute("commit")

    messagebox.showinfo("FIN", "GRACIAS POR PARTICIPAR")
    ventana.destroy()

#funcion encargada de iniciar el juego
def start():


        global l1,r1,r2,r3,r4,r5,preguntaSelecionada,respuestaseleccionada,out
        preguntaSelecionada, respuestaseleccionada=preguntas.generador_preguntas()
        #label que muestra la pregunta
        l1=Label(ventana,text=preguntaSelecionada[0],font=("cambria",20,"bold"))
        l1.place(x=20,y=50)
        lnivel=Label(ventana,text='nivel',font=("cambria",20,"bold"))
        lnivel.place(x=0,y=20)
        lnivel2 = Label(ventana, text=ques, font=("cambria", 20, "bold"))
        lnivel2.place(x=80, y=20)
        global i

        i=IntVar()
        i.set(-1)
        #botones de las preguntas
        r1 = Radiobutton(ventana,text=respuestaseleccionada[0][0][0],variable=i,  value=respuestaseleccionada[0][0][1],font="Verdana 16 bold",command=select)
        r1.place(x=150,y=150)
        r2 = Radiobutton(ventana, text=respuestaseleccionada[0][1][0],variable=i, value=respuestaseleccionada[0][1][1], font="Verdana 16 bold",command=select)
        r2.place(x=150, y=200)
        r3 = Radiobutton(ventana, text=respuestaseleccionada[0][2][0],variable=i, value=respuestaseleccionada[0][2][1], font="Verdana 16 bold",command=select)
        r3.place(x=150, y=250)
        r4 = Radiobutton(ventana, text=respuestaseleccionada[0][3][0],variable=i, value=respuestaseleccionada[0][3][1], font="Verdana 16 bold",command=select)
        r4.place(x=150, y=300)

        r5 = Button(ventana, text='salir', font="Verdana 16 bold", command=puntaje_acumulado)
        r5.place(x=180, y=400)



# funcion inicia el juego y cierra ventana de inicio
def remove():
    global l,b
    l.destroy()
    b.destroy()
    start()

#funcion ventana inicial
def welcome():
        global l,b

        l=Label(ventana,text="BIENVENIDO A QUIZAR",font=("cambria",30))
        l.place(x=30,y=150)
        b=Button(ventana,text="INICIAR",font=("cambria",20),command=remove)
        b.place(x=180,y=250)
#funcion para el login el jugador ingresa su usuario y contraseña
#si no esta registrado se debe registrar
def open_window():

    def check():
        nombre=Entry.get(e1)
        usuario=Entry.get(e2)
        password = Entry.get(e3)
        cpass = Entry.get(e4)

        if (nombre !="" and usuario!="" and password !="" and cpass!="" ):

            if (password != cpass):

                messagebox.showinfo("ERROR","no ha ingresado contraseña")
            else:
                con= mysql.connect(host="localhost",
                                   user="root",
                                   password="",
                                   database="quizar")
                cursor=con.cursor()

                #cursor.execute("INSERT INTO informacion(nombre,usuario,password,cpass) value("+nombre+","+usuario+","+password+","+cpass+")")
                cursor.execute("INSERT INTO quiz(nombre,usuario,password,cpass) VALUES('"+nombre+"','"+usuario+"','"+password+"','"+cpass+"')")
                cursor.execute("commit")
                messagebox.showinfo("INGRESO","Registro exitoso")

                con.close()
                x=rem0()
        else:
            messagebox.showinfo("Error","Por favor llenar todos los espacios" )
    global l,l1,l2,l3,l4,e1,e2,e3,e4,b1

    l=Label(ventana,text="REGISTRO",font=("cambria",18))
    l.place(x=150,y=50)

    l1=Label(ventana,text="Nombre",font=("cambria",15))
    l1.place(x=30,y=150)
    e1=Entry(ventana,width=25)
    e1.place(x=180,y=145)

    l2 = Label(ventana, text="Usuario",font=("cambria",15))
    l2.place(x=30, y= 200)
    e2 = Entry(ventana, width=25)
    e2.place(x=180, y=205)

    l3 = Label(ventana, text="Contraseña",font=("cambria",15))
    l3.place(x=30, y=250)
    e3 = Entry(ventana, width=25)
    e3.place(x=180, y=255)

    l4 = Label(ventana, text="Conformacion",font=("cambria",15))
    l4.place(x=30, y=300)
    l4 = Label(ventana, text="Contraseña", font=("cambria", 15))
    l4.place(x=30, y=330)
    e4 = Entry(ventana, width=25)
    e4.place(x=180, y=315)

    b1=Button(ventana,text="Enviar",font=("cambria",15),command=check)
    b1.place(x=180,y=400)

#funcion que cierra los procesos de ingreso
def rem1():
    global l1,l2,l0,e1,e2,b1,b2,fm

    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    open_window()

#funcion que cierra los procesos de ingreso
def rem():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    welcome()
#funcion que cierra los procesos de registro
def rem0():

    global l,l1,l2,l3,l4
    global e1,e2,e3,e4,b1

    l.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    e1.destroy()
    e3.destroy()
    e2.destroy()
    e4.destroy()
    b1.destroy()
    login()
#coneccion con la base de datos en mysql
con=mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="quizar")
cursor=con.cursor()
# funcion que comprara la clave y el usuario ingresado
def user_login(uname,passw):
    try:

        cursor.execute("select * from `quiz` where `nombre`='"+uname+"' and `password` ='"+passw+"'")

        return (cursor.fetchone())
    except:
        return False
#funcion de ingreso
def msg():

    global uname
    uname=Entry.get(e1)
    passw=Entry.get(e2)


    if (uname=="" or passw==""):
        messagebox.showinfo("INFORMACION ERRADA","llenar todos los espacios")
    else:

        res=user_login(uname,passw)

        if res:
            print(uname,passw)
            messagebox.showinfo("INGRESO","ha iniciado el juego")
            x=rem()
        else:
            messagebox.showinfo("INGRESO FALLIDO","ingreso fallido")
#inicia la ventana de la interfaz
ventana=Tk()
ventana.title("QUIZAR")
ventana.geometry("500x500")
#ventana de inicio
def login():
    global l1,l2,l0,e1,e2,b1,b2,fm

    l0=Label(ventana,text="Inicio",font=("cambria",20))
    l0.place(x=250,y=105)
    fm=Frame(ventana,relief=RIDGE)
    fm.place(x=0,y=150)

    l1=Label(fm,text="Username",padx=20,font=("cambria",20))
    l1.grid(row=1,column=0,padx=20,pady=40)
    e1=Entry(fm,font="Verdana")
    e1.grid(row=1,column=1,padx=20)

    l2 = Label(fm, text="Password",font=("cambria",20), padx=20)
    l2.grid(row=2, column=0, padx=20, pady=40)
    e2 = Entry(fm, font="verdana",show='x')
    e2.grid(row=2, column=1, padx=20)

    b1=Button(fm,text="Login",font="Verdana",command=msg)
    b1.grid(row=3,column=0,padx=50)

    b2 = Button(fm, text="Registrar", font="Verdana", command=rem1)
    b2.grid(row=3, column=1)

login()
ventana.mainloop()















