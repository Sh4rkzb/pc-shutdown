
import os
import customtkinter as ctk
import tkinter as tk

    
#janela
app = ctk.CTk() 
app.geometry('415x175+730+400') #tamanho da janela
app._set_appearance_mode("system") #aparencia da janela
app.title('Plugin aplicado com sucesso!') #titulo da janela
app.maxsize(width=415, height=175) #o tamanho maximo com a tela cheia
app.resizable(width=False, height=False) #diz se e permitido "esticar" a tela em horizontal ou vertical. False em ambos remove o modo tela cheia
#app.iconify() #abre e fecha a janela
#app.deiconify() #reabre a janela

#botao
def desligar():
  desligar = os.system("shutdown /s /t 1")#comando para desligar o pc
botao = ctk.CTkButton(app, text="ok", command= desligar)

botao.pack()
botao.place(x=150, y=60)

app.mainloop() #torna a linha de código um loop, para ficar printada na tela
