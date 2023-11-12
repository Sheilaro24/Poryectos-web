
#Vamos a crear una nueva version del ahorcado, donde vamos a partir de cero y debemos usar todo lo que hemos visto hasta ahora, programacion funcional, programacion orientada a objetos...
#Este ejercicio se hara en grupos de 3 personas
#La idea basica es el ahorcado con sus 7 posiciones, pero con estos nuevos requistos
#Debe estar orientado a objetos, debemos tener una estructura modular, donde se creen modulos paralas diferentes partes, pro ejemplo gestion de la pantalla
#La lista de palabras debe ser almacenada en un CSV que tenga cabecera y en cada fila una palabra
#Queremos que cada vez que se acabe una partida se guarde la puntuacion en un json, y asi poder tener un ranking, la puntuacion se calculara en base:
#Debemos tener un contador de tiempo, partimos con 100 puntos y cada 30 segundos que se tarde en resolver debemos restar 10 puntos, no se permiten puntuaciones negativas, para el tiepo hay que usar la libreria time
#Como optaivo montaremos el interfaz en tkinter, pero esto es optativo y si da tiempo

import csv
import json
import random
import time

palabras =  [["hola"], ["adios"], ["acierto"], ["python"], ["programacion"], ["objetos"]]
# Abrimos el archivo CSV en modo de escritura
with open("palabras.csv", "w+",newline="") as f:
    # Creamos un escritor CSV
    writer = csv.writer(f)
    # Escribimos la lista de palabras en el archivo CSV
    writer.writerows(palabras)


class Ahorcado:
    def __init__(self):
        self.palabras = self.cargar_palabras()
        self.palabra = self.elegir_palabra()
        self.letra_acertada = []
        self.error = 0
        self.puntuacion = 100
        

    def cargar_palabras(self):
        palabras = []
        with open('palabras.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                palabras.append(row[0])
        return palabras

    def elegir_palabra(self):
        return random.choice(self.palabras)

    def dibujar_ahorcado(self):
        ahorcado = [
            '''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
             /|\  |     
                  |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
             /|\  |     
             /    |
                  |
            =========''',
            '''
              +---+
              |   |
              O   |
             /|\  |     
             / \  |
                  |
            ========='''
        ]
        if self.error < len(ahorcado):
            return ahorcado[self.error]

    def mostrar_palabra(self):
        palabra_mostrada = ""
        for letra in self.palabra:
            if letra in self.letra_acertada:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
        return palabra_mostrada

    def adivinar_letra(self, letra):
        if letra in self.letra_acertada:
            print("Ya adivinaste esa letra, prueba con otra.")
        self.letra_acertada.append(letra)
        return letra in self.palabra

    def guardar_puntuacion(self):
        puntuacion = {
            "puntos": self.puntuacion,
            "tiempo": time.time()
        }
        with open('puntuaciones.json', 'a') as file:
            json.dump(puntuacion, file)
            file.write('\n')

    def juego_ahorcado(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        print("Tienes un máximo de 7 errores para adivinar la palabra.")
        while self.error < 7:
            palabra_mostrada = self.mostrar_palabra()
            print("Palabra: ", palabra_mostrada)
            letra = input("Adivina una letra: ").lower()
            if len(letra) != 1 or not letra.isalpha():
                print("Introduce una única letra.")
                continue
            if not self.adivinar_letra(letra):
                print(self.dibujar_ahorcado())
                self.error += 1
                self.puntuacion -= 10
                if self.puntuacion < 0:
                    self.puntuacion = 0
            if self.palabra == self.mostrar_palabra():
                print("¡Felicidades! Has adivinado la palabra: ", self.palabra)
                self.guardar_puntuacion()
                break
        else:
            print("MUERTO!  ", self.palabra)
            self.guardar_puntuacion()
LookupError
juego = Ahorcado()
juego.juego_ahorcado()
