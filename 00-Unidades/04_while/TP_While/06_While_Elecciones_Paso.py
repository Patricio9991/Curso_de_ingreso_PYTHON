import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        maximo_votos = 0
        minimo_votos = 0

        nombre_voto_maximo = ''
        nombre_voto_minimo = ''

        promedio_edades = 0

        acumulador_votos = 0
        acumulador_edades = 0

        iterador = 0

        while True:
            nombre = prompt("","Ingrese nombre del candidato")

            if nombre == None:
                break

            edad = prompt("","Edad del candidato")
            edad = int(edad)

            while edad < 25:
                alert("","Edad invalida, vuelva a ingresar")
                edad = prompt("","Ingrese su edad")
                edad = int(edad)

            votos = prompt("","Cantidad votos")
            votos = int(votos)

            while votos <= -1:
                alert("","votos invalidos, vuelva a ingresar")
                votos = prompt("","Ingrese su votos")
                votos = int(votos)


            if iterador == 0:
                maximo_votos = votos
                minimo_votos = votos
                nombre_voto_maximo = nombre
                nombre_voto_minimo = nombre

            else:
                if votos > maximo_votos:
                    maximo_votos = votos
                    nombre_voto_maximo = nombre

                if votos <minimo_votos:    
                    minimo_votos = votos  
                    nombre_voto_minimo = nombre 


            acumulador_votos +=votos
            acumulador_edades +=edad

            iterador +=1

        promedio_edades = acumulador_edades / iterador    

        alert("",f"maximo votos: {maximo_votos}, nombre: {nombre_voto_maximo}")
        alert("",f"minimo votos: {minimo_votos}, nombre: {nombre_voto_minimo}")
        alert("",f"El promedio de edades es: {promedio_edades}")
        alert("",f"Total votos emitidos: {acumulador_votos}")
                    
             


            
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
