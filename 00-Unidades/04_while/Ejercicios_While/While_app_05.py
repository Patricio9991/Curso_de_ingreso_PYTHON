import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Patricio
apellido: Pucheta
---
Ejercicio: while_05
---
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). 
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra = prompt("UTN","Ingrese letra en mayuscula")
        letra = letra.upper() #para asegurarme de que se ingrese en mayus.

        print(letra)
        while letra != "U" and letra != "T" and letra != "N":
            msg = "Ingrese una letra valida"
            alert("UTN",msg)
            letra = prompt("UTN","Ingrese letra en mayuscula")
            letra = letra.upper()
            
        alert("UTN","Letra correcta")    
        pass
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()