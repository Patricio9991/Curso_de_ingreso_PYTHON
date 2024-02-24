import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. X Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. X Nombre del postulante Jr con menor edad.
c. X Promedio de edades por género.
d. XTecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_punto_a = 0

        contador_jr = 0
        minimo_edad_jr = 0 
        flag_minimo_jr = 0

        contador_F = 0
        contador_M = 0
        contador_NB = 0

        acumulador_edad_F = 0
        acumulador_edad_M = 0
        acumulador_edad_NB = 0

        contador_python = 0
        contador_js = 0
        contador_asp = 0
        
        for i in range(0,10):
            nombre = input("Ingrese su nombre: ")
            edad = input("Ingrese su edad: ")
            edad = int(edad)

            while edad < 18:
                edad = input("Reingrese su edad: ")
                edad = int(edad)

            genero = input("Ingrese su genero: ")
            
            while genero != "M" and genero != "F" and genero != "NB":
                genero = input("Reingrese su genero, no se ofenda: ")

            tecnologia = input("Ingrese su tecnologia: ")
            
            while tecnologia != "python" and tecnologia != "js" and tecnologia != "asp .net":
                tecnologia = input("Reingrese su tecnologia: ")

            puesto = input("Ingrese su puesto: ")
            
            while puesto != "jr" and puesto != "ssr" and puesto != "sr":
                puesto = input("Reingrese su puesto: ")

            
            if genero == "F":
                contador_F += 1
                acumulador_edad_F += edad
                if puesto == "jr":
                    contador_jr +=1
                    
                
            elif genero == "M":
                contador_M += 1
                acumulador_edad_M += edad

                if puesto == "jr":
                    contador_jr +=1
                
            else:
                contador_NB += 1
                acumulador_edad_NB += edad

                if puesto == "jr":
                    contador_jr +=1

            #   a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            # cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            # if genero == "NB" and (tecnologia == "asp .net" or tecnologia== "js") and (edad >=25 and edad <= 40) and puesto == "ssr":

                if (tecnologia == "asp .net" or tecnologia== "js") and (edad >=25 and edad <= 40) and puesto == "ssr":
                    contador_punto_a +=1

            #b. Nombre del postulante Jr con menor edad.  

            if edad < minimo_edad_jr or flag_minimo_jr == False:
                minimo_edad_jr = edad
                nombre_minimo_edad_jr = nombre
                flag_minimo_jr = True  

            #d. Tecnologia con mas postulantes (solo hay una).   
            match tecnologia:
                case "python":
                    contador_python +=1
                case "js":
                    contador_js +=1
                case "asp .net":
                    contador_asp +=1

                

            
        print(f"Femenino: {contador_F} | Masculino: {contador_M} | NB: {contador_NB}")

        print(f"a) {contador_punto_a}") 

        print(f"b) El jr de menor edad tiene {minimo_edad_jr} años y se llama {nombre_minimo_edad_jr}")

        #c. Promedio de edades por género.
        promedio_F = acumulador_edad_F / contador_F
        promedio_M = acumulador_edad_M / contador_M
        promedio_NB = acumulador_edad_NB / contador_NB

        print(f"c) Promedio edades Femenino: {promedio_F} | Promedio edades Masculino: {promedio_M} | Promedio edades NB: {promedio_NB}")

        #d continuacion

        if contador_asp > contador_js and contador_asp > contador_python:
            msg = "la teconologia con mas postulantes es asp .net"
        elif contador_js > contador_python:
            msg = "la teconologia con mas postulantes es JS"
        else:
            msg = "la teconologia con mas postulantes es python"

        print(f"d) {msg}")

        #e. Porcentaje de postulantes de cada genero.
        total_postulantes = contador_F + contador_M + contador_NB
        porcentaje_F = (contador_F*100)/total_postulantes
        porcentaje_M = (contador_M*100)/total_postulantes
        porcentaje_NB = (contador_NB*100)/total_postulantes

        print(f"e) Femenino porcentaje: {porcentaje_F} | Masculino porcentaje: {porcentaje_M} | NB porcentaje: {porcentaje_NB}")




                
                


                

        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
