import math
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os

root = Tk()
root.title("Calculadora Cientifica")
root.configure(background ="black") #referente a cor da calculadora 
root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
root.geometry("800x600+0+0")#695x568 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior
file = open("Log da Calculadora.txt", "a+")


nb = ttk.Notebook(root)#Criação de abas
nb.place(x=0, y=0, width=800, height=800)#tamanho das abas
aba1 = Frame(nb)
nb.add(aba1, text="Calculadora científica")
aba2 = Frame(nb)
nb.add(aba2, text="Ver ajuda")
aba3 = Frame(nb)
nb.add(aba3, text="Histórico")


class Operações_Elementares(): #Vai cuidar de todas as operações mais simples e conversões
    def __init__(self):
        self.total=0
        self.atual=''
        self.valor=True
        self.chk_soma=False
        self.op=''
        self.resultado=False
    
    def display(self, value): # Controla o que está sendo demonstrado
        Keyboard.entrada.delete(0, END)
        Keyboard.entrada.insert(0, value)
    
    def num_entrada(self, num):  #Modifica os números na Keyboard.entrada para contas rápidas
        self.resultado=False
        num1=Keyboard.entrada.get()
        num2=str(num)
        if self.valor:
            self.atual = num2
            self.valor=False
        else:
            if num2 == '.':
                if num2 in num1:
                    return
            self.atual = num1+num2
        self.display(self.atual)
        Keyboard.persistencia(num)
  
    def operação(self, op): # Chama as operações se baseando nos botões
        self.atual = float(self.atual)
        if self.chk_soma:
            self.função()
        elif not self.resultado:
            self.total=self.atual
            self.valor=True
        self.chk_soma=True
        self.op=op
        self.resultado=False
        Keyboard.persistencia(self.op)
  
    def somatório(self): # Faz o uso de diferentes entradas
        self.resultado=True
        self.atual=float(self.atual)
        if self.chk_soma==True:
            self.função()
        else:
            self.total=float(Keyboard.entrada.get())

    def função(self): # Faz as operações se baseando nos botões com os comandos atrelados
        if self.op == "+":
            self.total += self.atual
        if self.op == "-":
            self.total -= self.atual
        if self.op == "*":
            self.total *= self.atual
        if self.op == "/":
            self.total /= self.atual
        if self.op == "%":
            self.total %= self.atual
        self.valor=True
        self.chk_soma=False
        self.display(self.total)
        Keyboard.persistencia(" = ")
        Keyboard.persistencia(float(self.total))
        Keyboard.persistencia("\n")
        Keyboard.close()
        Keyboard.open()

    def limpar(self): #Função que limpa o display
        self.resultado = False
        self.atual = "0"
        self.display(0)
        self.valor=True
  
    def limpar_tudo(self): #Função que limpa as funções
        self.limpar()
        self.total=0

#==========================================================================Conversões Rápidas==========================================================================
  
    def pi(self): #Converte π
        self.resultado =  False
        self.atual = math.pi
        self.display(self.atual)
        Keyboard.persistencia(self.atual)
        Keyboard.persistencia("\n")

    def euler(self): #Converte e
        self.resultado =  False
        self.atual = math.e
        self.display(self.atual)
        Keyboard.persistencia(self.atual)
        Keyboard.persistencia("\n")

    def raiz(self): #Faz a raiz do número no resultado
        self.resultado = False
        self.atual = math.sqrt(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia("^1/2 = ")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
  
    def cos(self): #Faz o Coseno do número no resultado
        self.resultado = False
        self.atual = math.cos(math.radians(float(Keyboard.entrada.get())))
        self.display(self.atual)
        Keyboard.persistencia(" = arccos(")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia(")\n")

    def tan(self): #Faz a Tangente do número no resultado
        self.resultado = False
        self.atual = math.tan(math.radians(float(Keyboard.entrada.get())))
        self.display(self.atual)
        Keyboard.persistencia(" = arctan(")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia(")\n")

    def seno(self): #Faz o Seno do número no resultado
        self.resultado = False
        self.atual = math.sin(math.radians(float(Keyboard.entrada.get())))
        self.display(self.atual)
        Keyboard.persistencia(" = arcsen(")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia(")\n")
  
    def log(self): #Faz o Log do número no resultado
        self.resultado = False
        self.atual = math.log(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia(" = ")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
  
    def exp(self): #Faz o Exponencial na base e do número no resultado
        self.resultado = False
        self.atual = math.exp(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia(" = ln(")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia(")\n")

    def quad(self): #Converte radianos em graus do número no resultado
        self.resultado = False
        self.atual = math.pow(float(Keyboard.entrada.get()),2)
        self.display(self.atual)
        Keyboard.persistencia(" = ")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
  
    def log2(self): #Faz o Log de base 2 do número no resultado
        self.resultado = False
        self.atual = math.log2(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia(" = 2^")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
        
  
    def log10(self): #Faz o Log de base 10 do número no resultado
        self.resultado = False
        self.atual = math.log10(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia(" = 10^")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
  
    def log1p(self): #Faz o Log na base e de 1+ o número no resultado
        self.resultado = False
        self.atual = math.log1p(float(Keyboard.entrada.get()))
        self.display(self.atual)
        Keyboard.persistencia(" = ")
        Keyboard.persistencia(float(self.atual))
        Keyboard.persistencia("\n")
  
valor_adicionado = Operações_Elementares()

#====================================================Interface grafica================================================

abas = [aba1]

#botoes calc simples 
for aba in abas:
    if aba == aba1:

        numberpadkk = "789456123"
        i=0
        btn = []
        for j in range(2,5):
            for k in range(3):
                btn.append(Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white",bg="grey32", bd=4, text =numberpadkk[i]))
                btn[i].grid(row = j, column=k,pady=1)
                btn[i]["command"]=lambda x=numberpadkk[i]:valor_adicionado.num_entrada(x)
                i+=1
        btnlimpar = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command= lambda: valor_adicionado.limpar(), text = chr(67), bg="grey58").grid(row = 1, column=0,pady=1)

        btnlimptudo = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command= lambda: valor_adicionado.limpar_tudo(), text = chr(67)+ chr(69), bg="grey58").grid(row = 1, column=1,pady=1)

        btnraiz = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.raiz, text = "√", bg="grey58").grid(row = 1, column=2,pady=1)

        btnsoma = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("+"), text = "+", bg="chocolate1").grid(row = 1, column=3,pady=1)

        btnsubt = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("-"), text = "-", bg="chocolate1").grid(row = 2, column=3,pady=2)

        btnmult = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("*"), text = "*", bg="chocolate1").grid(row = 3, column=3,pady=3)

        btndiv = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("/"), text = ":", bg="chocolate1").grid(row = 4, column=3,pady=4)

        #problema
        btnquad = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command= lambda:valor_adicionado.quad(), text = "^2", bg="grey58").grid(row = 5, column=0,pady=1)

        btnzero = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.num_entrada(0), text = "0", bg="grey32").grid(row = 5, column=1,pady=1) 

        btnponto = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.num_entrada("."), text = ".", bg="grey58").grid(row = 5, column=2,pady=1)

        btnigual = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command= lambda: [valor_adicionado.somatório()], text = "=", bg="chocolate1").grid(row = 5, column=3,pady=1)


        #============================================CALC-CIENTIFICA==========================================================

        #botoes calc cientifica

        btnpi = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.pi, text = "π", bg="grey58").grid(row = 1, column=4,pady=1)

        btnsen = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.seno, text = "sen", bg="grey58").grid(row = 2, column=4,pady=1)

        btncos = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.cos, text = "cos", bg="grey58").grid(row = 3, column=4,pady=1)

        btntg = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.tan, text = "tg", bg="grey58").grid(row = 4, column=4,pady=1)

        btne = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.euler, text = "e", bg="grey58").grid(row = 5, column=4,pady=1)

        btnlog = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.log, text = "log", bg="grey58").grid(row = 1, column=5,pady=1)

        btnlog2 = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "log2",command=valor_adicionado.log2, bg="grey58").grid(row = 2, column=5,pady=1)

        btnlog10 = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "log10",command=valor_adicionado.log10, bg="grey58").grid(row = 3, column=5,pady=1)

        btnloglp = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4,command=valor_adicionado.log1p, text = "ln", bg="grey58").grid(row = 4, column=5,pady=1)
        
        btnexpo = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "exp",command=valor_adicionado.exp, bg="grey58").grid(row = 5, column=5,pady=1)

        btnx = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "x", bg="grey58").grid(row = 0, column=6,pady=1)

        btnparent1 = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "(", bg="grey58").grid(row = 1, column=6,pady=1)

        btnparent2 = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = ")", bg="grey58").grid(row = 2, column=6,pady=1)

        btnderiv = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "dy/dx", bg="grey58").grid(row = 3, column=6,pady=1)

        btnlim = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "lim", bg="grey58").grid(row = 4, column=6,pady=1)

        btninte = Button(aba, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "∫", bg="grey58").grid(row = 5, column=6,pady=1)

#================================================================Display=======================================================================================


class Keyboard(): #Traduz as letras e símbolos e grava no arquivo de histórico
    
    def __init__(self, variavel):
        self.pos_neg = bool # True - positivo; False - negativo
        self.str = variavel # Atributo que armazena a variavel passada pela interface (a espera de definições de atributos)
        self.x = bool # Atributo que sinaliza a presença do x no proximo objeto
        self.potencia = 1 # Atributo que sinaliza que o objeto se trata de uma potencia de uma função
    

    def close():
        arquivo.close()

    def open():
        arquivo = open(Keyboard.caminho+"/Log da Calculadora.txt", "a+")

    def setPotencia(self, potencia): # Metodo que atribui ao objeto alguma potencia numérica
        self.potencia = potencia
    
    def setStr(self, str):
        self.str = str

    def getX(self):
        return self.x

    def getPotencia(self):
        return self.potencia

    def getStr(self):
        return self.str
    
    def setPosNeg(self, pos_neg):
        self.pos_neg = pos_neg

    def setX(self, x):
        self.x = x

    def getPosNeg(self):
        return self.pos_neg

    def setElevado(self, valor):
        self.potencia = valor

    def getElevado(self):
        return self.potencia

    caminho=os.getcwd()

    def persistencia(dado):  #Abre um arquivo txt e grava o dado no arquivo
        with open(Keyboard.caminho+"/Log da Calculadora.txt", "a") as log:
            dado=str(dado)
            log.writelines(dado)

    entrada = Entry(aba, font = ("arial",20,"bold"), bg="white", bd=30, width=40,justify=RIGHT)
    entrada.grid(row = 0, column=0, columnspan=6,pady=1)
    entrada.insert(0,"0")

#====================================================Aba Ver Ajuda=====================================================================================================

labels1 = Label(aba2,text="Casos de Limites:\n> balabablabla\n> blabalbablabalb\n> blbablablalbabalba", bd=2, font=25, borderwidth=2, relief="flat").grid(column = 0, row = 1,padx = 30,pady = 30,sticky = "e")
labels2 = Label(aba2,text="Cálculos possiveis:\n> Aritiméticos\n> Funções\n> Valor das Constantes",bd=2, font=25, borderwidth=2, relief="flat").grid(column = 0, row = 0, padx = 30,pady = 30,sticky="e")
labels3 = Label(aba2,text="Casos de Derivadas:\n> blabalbblaboalal\n> llolboalbaoblaool \n> blblalbablalbala",bd=2, font=25, borderwidth=2, relief="flat").grid(column = 0, row = 2,padx = 30,pady = 30,sticky="e")
#===================================================Aba Historico======================================================================================================
arquivo = open(Keyboard.caminho+"/Log da Calculadora.txt", "r")
historico = arquivo.readlines()
listbox_widget = tkinter.Listbox(aba3)
for entry in historico:
    listbox_widget.insert(tkinter.END, entry)
listbox_widget.pack(side = LEFT, expand = True, fill = BOTH)
arquivo.close()
#====================================================MENU==============================================================================================================


def saida():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica","Deseja sair?")#abre uma caixa com a msg escrita
    if sair > 0:
        #file.close()
        root.destroy()
        return


menubar = Menu(aba1)
padraomenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Sair" , command=saida)#adiciona a opcao do usuario clicar em "opções"


root.config(menu = menubar)
root.mainloop()
