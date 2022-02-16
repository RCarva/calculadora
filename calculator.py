from cgitb import text
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculadora Cientifica")
root.configure(background ="grey35") #referente a cor da calculadora 
root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
root.geometry("480x568+450+90")#480x568 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior

calculo = Frame(root)
calculo.grid()

#====================================================Interface grafica================================================


txtdisplay = Entry(calculo, font = ("arial",20,"bold"), bg="snow", bd=30, width=28,justify=RIGHT)
txtdisplay.grid(row = 0, column=0, columnspan=4,pady=1)
txtdisplay.insert(0,"0")

numberpadkk = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="ivory2", bd=4,bg="grey32", text =numberpadkk[i]))
        btn[i].grid(row = j, column=k,pady=1)
        i+=1

#botoes calc simples 
btnlimpar = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = chr(67), bg="grey58").grid(row = 1, column=0,pady=1)

btnlimptudo = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = chr(67)+ chr(69), bg="grey58").grid(row = 1, column=1,pady=1)

btnraiz = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "√", bg="grey58").grid(row = 1, column=2,pady=1)

btnsoma = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "+", bg="chocolate1").grid(row = 1, column=3,pady=1)

btnsubt = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "-", bg="chocolate1").grid(row = 2, column=3,pady=2)

btnmult = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "x", bg="chocolate1").grid(row = 3, column=3,pady=3)

btndiv = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = ":", bg="chocolate1").grid(row = 4, column=3,pady=4)

btnpotencia = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "", bg="grey58").grid(row = 5, column=0,pady=1)

btnzero = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "0").grid(row = 5, column=1,pady=1) # nao sei se funcionaria dessa forma

btnponto = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = ".", bg="grey58").grid(row = 5, column=2,pady=1)

btnigual = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "=", bg="chocolate1").grid(row = 5, column=3,pady=1)


#============================================CALC-CIENTIFICA==========================================================

#botoes calc cientifica
btnparent1 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "(", bg="grey58").grid(row = 0, column=4,pady=1)

btnparent2 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = ")", bg="grey58").grid(row = 0, column=5,pady=1)

btnpi = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "π", bg="grey58").grid(row = 1, column=4,pady=1)

btnsen = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "sen", bg="grey58").grid(row = 2, column=4,pady=1)

btncos = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "cos", bg="grey58").grid(row = 3, column=4,pady=1)

btntg = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "tg", bg="grey58").grid(row = 4, column=4,pady=1)

btne = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "e", bg="grey58").grid(row = 5, column=4,pady=1)

btnlog = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "log", bg="grey58").grid(row = 1, column=5,pady=1)

btnln = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "ln", bg="grey58").grid(row = 2, column=5,pady=1)

btnlimite = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "lim", bg="grey58").grid(row = 3, column=5,pady=1)

btnderiv = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "dy/dx", bg="grey58").grid(row = 4, column=5,pady=1)

btnintegral = Button(calculo, width=6, height=2, font=("arial", 20, "bold"), bd=4,fg="white", text = "∫", bg="grey58").grid(row = 5, column=5,pady=1)


#====================================================MENU=============================================================


def saida():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica","Deseja sair?")#abre uma caixa com a msg escrita
    if sair > 0:
        root.destroy()
        return

def cientifica():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("716x568+450+90")

def padrao():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("480x568+450+90")

menubar = Menu(calculo)
padraomenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Opções" , menu=padraomenu)#adiciona a opcao do usuario clicar em "opções"
padraomenu.add_command(label = "Calculadora Padrão", command= padrao)
padraomenu.add_command(label = "Calculadora científica", command= cientifica)
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
