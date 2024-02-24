import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        #G)Valor maximo
        #H)Valor minimo
        import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Patricio
apellido: Pucheta
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. Valor maximo 
    H. Valor minimo indicando en que iteracion se encontro

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        diferencia_negativos_positivos = 0
        maximo = 0
        minimo = 0
        bandera_numero = False
        contador = 0
        minimo_positivo = 0
        bandera_minimo_positivo = False
        
        


        while True:
            numero = prompt("Utn" , "Ingrese el número")
            if numero == None:
                break
            numero = float(numero)
            
            contador += 1
            
            if numero > 0 :
                cantidad_positivos += 1
                suma_positivos += numero
                if numero < minimo_positivo or bandera_minimo_positivo == False:
                    print (numero,minimo_positivo,bandera_minimo_positivo)
                    minimo_positivo = numero
                    bandera_minimo_positivo = True
                print (bandera_minimo_positivo)    
                    
            elif numero == 0:
                cantidad_ceros += 1
            else:
                cantidad_negativos += 1
                suma_negativos += numero
                
                
            if numero > maximo or bandera_numero == False:
                maximo = numero
                
            if numero < minimo or bandera_numero == False:
                minimo = numero
                bandera_numero = True
                posicion_minimo = contador

        #variantes vistas en dojo
        print(f"El maximo es {maximo}")
        print(f"El minimo positivo es {minimo_positivo}")        
        print(f"El valor minimo general esta en la posicion {posicion_minimo}")
                
                

        diferencia_negativos_positivos = abs(cantidad_positivos - cantidad_negativos)
        
        msg = f"Positivos: {suma_positivos}, Negativos: {suma_negativos}, Cantidad de ceros: {cantidad_ceros}, Cantidad de positivos: {cantidad_positivos}, Cantidad de negativos: {cantidad_negativos} y Diferencia entre positivos y negativos: {diferencia_negativos_positivos} "

        alert("UTN",msg)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
