from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculadora Cientifica")
root.configure(background ="powder blue") #referente a cor da calculadora 
root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
root.geometry("480x568+450+90")#480x568 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior

calculo = Frame(root)
calculo.grid()

#====================================================MENU=============================================================


def saida():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica","Deseja sair?")#abre uma caixa com a msg escrita
    if sair > 0:
        root.destroy()
        return

menubar = Menu(calculo)
padraomenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Opções" , menu=padraomenu)#adiciona a opcao do usuario clicar em "opções"
padraomenu.add_command(label = "Calculadora Padrão")
padraomenu.add_command(label = "Calculadora científica")
padraomenu.add_separator()
padraomenu.add_command(label = "Sair", command= saida)

configmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Configurações" , menu=configmenu)#adiciona a opcao do usuario clicar em "configurações"
configmenu.add_command(label = "Cortar")
configmenu.add_command(label = "Copiar")
configmenu.add_separator()
configmenu.add_command(label = "Inserir")

ajudamenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Ajuda" , menu=ajudamenu)#adiciona a opcao do usuario clicar em "ajuda"
ajudamenu.add_command(label = "Ver ajuda")

root.config(menu = menubar)
root.mainloop()