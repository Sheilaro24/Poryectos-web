#Crear un directorio
#importar libreria os especial para manejar archivos
import os
#en mayuscula, es una constate que no se debe modificar
CARPETA= "contactos/"
EXTENSION= ".txt" #extension de archivos

#contactos, crear una clase
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        #atributos
        self.nombre=nombre
        self.telefono=telefono
        self.categoria=categoria

#principal, donde se llaman a las demas
def app():
    #revisa si la carpeta existe o no
    crear_directorio()
    # mostrar menu de opciones
    mostrar_opciones()

#preguntar al usuario la accion a realizar
    preguntar=True

    while preguntar:
        opcion=input("seleccione una opción: \r\n")
        opcion= int(opcion) #convertir un string a un entero

     #ejecutar opciones
        if opcion ==1:
            agregar_contacto()
            preguntar=False
        elif opcion ==2:
            editar_contacto()
            preguntar = False
        elif opcion ==3:
            mostrar_contactos()
            preguntar = False
        elif opcion ==4:
            buscar_contacto()
            preguntar = False
        elif opcion ==5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opción no valida, elija del 1 al 5")

def eliminar_contacto():
    nombre = input("Selecciones el contacto que deseas eliminar: \r\n")
    try:
        os.remove(CARPETA + nombre+ EXTENSION)
        print("Contacto eliminado")
    except expression as identifier:
        print("El contacto no existe")
    app()
def buscar_contacto():
    nombre= input("Selecciones el contacto que deseas buscar: \r\n  ")
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print("\r\n Información del contacto: \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("El archivo no existe")
        print(IOError)

    app()
def mostrar_contactos():
   archivos=os.listdir(CARPETA)
   archivos_txt= [i for i in archivos if i.endswith(EXTENSION)]

   for archivo in archivos_txt:
       with open(CARPETA + archivo) as contacto:
           for linea in contacto:
               print( linea.rstrip())

           print("\r\n")
def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior= input("Nombre del contacto a editar:  \r\n")
    # Revisar abtes de editar
    existe = exite_contacto(nombre_anterior)
    if existe:
        print("puedes editar")
    else:
        print("Ese contacto no existe")

def agregar_contacto():
    print("Escribe los datos para agregar un nuevo contacto.")
    nombre_contacto= input("Nombre del contacto: ")
    #Revisar si el contacto ya existe
    existe=os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    if not existe:
    #crea los archivos contactos\Sheila.txt / w para permitir escribir
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
           #resto de los campos
            telefono_contacto=input("Agrega el Teléfono: \r\n")
            categoria_contacto= input("Categoría Contacto: \r\n")

            #instaciar la clase:
            contacto= Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archvio

            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

            #Mostrar mensaje de exito
            print("\r\n Contacto creado Correctamente \r\n")
    else:
        print("Ese contacto ya existe")

    #Reiniciar la app
    app()

#mostrar menu de opciones
def mostrar_opciones():
    print("Seleccione del Menú lo que deseas hacer")
    print("1) Agregar nuevo contacto")
    print("2) Editar contacto")
    print("3) Ver contactos")
    print("4) Buscar contacto")
    print("5) Eliminar contacto ")
def crear_directorio():
    if not os.path.exists(CARPETA):
        # crear carpeta si no existe
        os.makedirs(CARPETA)

def exite_contacto (nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()