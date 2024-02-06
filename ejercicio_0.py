from customtkinter import * 

app = CTk()

def button_on_click():
    print("Python instalado")


button = CTkButton(master=app, text="Click Here", command=button_on_click)
button.grid()

app.mainloop()