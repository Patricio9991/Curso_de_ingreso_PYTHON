import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Patricio    
apellido: Pucheta
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
#     Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
# de los numeros pares comprendidos entre el 1 y el 10.
    def btn_mostrar_iteracion_on_click(self):
        #primero lo hice asi:

        # iterador = 0
        # acumulador_pares = 0

        # while iterador < 10:
        #     numero = iterador+1
        #     print(iterador+1)
        #     if numero % 2 == 0:
        #         acumulador_pares += numero
                
        #     iterador +=1    

        #y despues asi para tener la otra alternativa:
        iterador = 2
        acumulador_pares = 0

        while iterador <=10:
            acumulador_pares += iterador
            iterador += 2



        alert("UTN", f"La suma es {acumulador_pares}")
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()