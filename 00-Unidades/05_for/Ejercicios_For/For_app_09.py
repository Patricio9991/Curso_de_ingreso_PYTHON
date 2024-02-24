import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre:
apellido:
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_aleatorio = 6

        for i in range(1,8):
            numero_usuario = prompt("",f"Ingrese un numero, intento {i}")
            numero_usuario = int(numero_usuario)
                
            if numero_aleatorio == numero_usuario and i == 1:
                print("Usted es un psíquico")
                break
            else:
                match i:
                    case 2:
                        if numero_aleatorio == numero_usuario:
                            print("Excelente percepción")
                            break
                    case 3:
                        if numero_aleatorio == numero_usuario:
                            print("Esto es suerte")
                            break
                    case 4|5|6:
                        if numero_aleatorio == numero_usuario:
                            print("Excelente tecnica")
                            break
                    case 7:
                        print("Perdiste, suerte para la próxima")
                        
                if i == 7 and numero_usuario != numero_aleatorio:
                    if numero_usuario > numero_aleatorio:
                        print(f"Se paso del numero secreto")
                    else:
                        print(f"Le falto para el numero secreto")

            

        pass
                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()