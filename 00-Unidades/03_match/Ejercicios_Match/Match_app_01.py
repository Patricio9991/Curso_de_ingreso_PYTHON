import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''

nombre: Patricio    
apellido: Pucheta
---
Ejercicio: Match_01
---
Enunciado:
Obtener el valor del mes seleccionado en el combobox_mes y  
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’

En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes =  self.combobox_mes.get()
        msg= 'No conice con ningun case'
        match mes:
            case "Enero":
                 msg = "que comiences bien el año!!!"
            case "Marzo":
                msg = "a clases!!"
            case "Julio":
                msg = "se vienen las vacaciones!!"
            case "Diciembre":
                msg = "Felices fiestas!!!" 

                


        alert("UTN",msg)
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()