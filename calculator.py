import math
from cgitb import text
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Calculadora Cientifica")
root.configure(background ="powder blue") #referente a cor da calculadora 
root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
root.geometry("718x568+450+90")#480x568 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior

calculo = Frame(root)
calculo.grid()


class Operações_Elementares(): #Vai cuidar de todas as operações mais simples e conversões
    def __init__(self):
        self.total=0
        self.atual=''
        self.valor=True
        self.chk_soma=False
        self.op=''
        self.resultado=False
    
    def display(self, value): # Controla o que está sendo demonstrado
        entrada.delete(0, END)
        entrada.insert(0, value)
    
    def num_entrada(self, num):  #Modifica os números na entrada para contas rápidas
        self.resultado=False
        num1=entrada.get()
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
  
    def somatório(self): # Faz o uso de diferentes entradas
        self.resultado=True
        self.atual=float(self.atual)
        if self.chk_soma==True:
            self.função()
        else:
            self.total=float(entrada.get())

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

    def euler(self): #Converte e
        self.resultado =  False
        self.atual = math.e
        self.display(self.atual)

    def raiz(self): #Faz a raiz do número no resultado
        self.resultado = False
        self.atual = math.sqrt(float(entrada.get()))
        self.display(self.atual)
  
    def cos(self): #Faz o Coseno do número no resultado
        self.resultado = False
        self.atual = math.cos(math.radians(float(entrada.get())))
        self.display(self.atual)

    def tan(self): #Faz a Tangente do número no resultado
        self.resultado = False
        self.atual = math.tan(math.radians(float(entrada.get())))
        self.display(self.atual)

    def seno(self): #Faz o Seno do número no resultado
        self.resultado = False
        self.atual = math.sin(math.radians(float(entrada.get())))
        self.display(self.atual)
  
    def log(self): #Faz o Log do número no resultado
        self.resultado = False
        self.atual = math.log(float(entrada.get()))
        self.display(self.atual)

    def quad(self):
        self.resultado=False
        self.atual = math.pow(float(entrada.get()),2)
        self.display(self.atual)
  
    def exp(self): #Faz o Exponencial na base e do número no resultado
        self.resultado = False
        self.atual = math.exp(float(entrada.get()))
        self.display(self.atual)

    def graus(self): #Converte radianos em graus do número no resultado
        self.resultado = False
        self.atual = math.degrees(float(entrada.get()))
        self.display(self.atual)
  
    def log2(self): #Faz o Log de base 2 do número no resultado
        self.resultado = False
        self.atual = math.log2(float(entrada.get()))
        self.display(self.atual)
  
    def log10(self): #Faz o Log de base 10 do número no resultado
        self.resultado = False
        self.atual = math.log10(float(entrada.get()))
        self.display(self.atual)
    
  
    def log1p(self): #Faz o Log na base e de 1+ o número no resultado
        self.resultado = False
        self.atual = math.log1p(float(entrada.get()))
        self.display(self.atual)
  
valor_adicionado = Operações_Elementares()

#====================================================Interface grafica================================================


entrada = Entry(calculo, font = ("arial",20,"bold"), bg="white", bd=30, width=28,justify=RIGHT)
entrada.grid(row = 0, column=0, columnspan=4,pady=1)
entrada.insert(0,"0")

numberpadkk = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white",bg="grey32", bd=4, text =numberpadkk[i]))
        btn[i].grid(row = j, column=k,pady=1)
        btn[i]["command"]=lambda x=numberpadkk[i]:valor_adicionado.num_entrada(x)
        i+=1

#botoes calc simples 
btnlimpar = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.limpar, text = chr(67), bg="grey52").grid(row = 1, column=0,pady=1)

btnlimptudo = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.limpar_tudo, text = chr(67)+ chr(69), bg="grey52").grid(row = 1, column=1,pady=1)

btnraiz = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.raiz, text = "√", bg="grey58").grid(row = 1, column=2,pady=1)

btnsoma = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("+"), text = "+", bg="chocolate1").grid(row = 1, column=3,pady=1)

btnsubt = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("-"), text = "-", bg="chocolate1").grid(row = 2, column=3,pady=2)

btnmult = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("*"), text = "x", bg="chocolate1").grid(row = 3, column=3,pady=3)

btndiv = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.operação("/"), text = ":", bg="chocolate1").grid(row = 4, column=3,pady=4)

btnpocent = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda:valor_adicionado.operação("%"),  text = "%", bg="grey58").grid(row = 5, column=0,pady=1)

btnzero = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.num_entrada(0), text = "0", bg="grey32").grid(row = 5, column=1,pady=1) # nao sei se funcionaria dessa forma

btnponto = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=lambda: valor_adicionado.num_entrada(","), text = ".", bg="grey58").grid(row = 5, column=2,pady=1)

btnigual = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.somatório, text = "=", bg="chocolate1").grid(row = 5, column=3,pady=1)


#============================================CALC-CIENTIFICA==========================================================

#botoes calc cientifica
btnparent1 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "(", bg="grey58").grid(row = 0, column=4,pady=1)

btnparent2 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = ")", bg="grey58").grid(row = 0, column=5,pady=1)

btnpi = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.pi, text = "π", bg="grey58").grid(row = 1, column=4,pady=1)

btnsen = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.seno, text = "sen", bg="grey58").grid(row = 2, column=4,pady=1)

btncos = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.cos, text = "cos", bg="grey58").grid(row = 3, column=4,pady=1)

btntg = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.tan, text = "tg", bg="grey58").grid(row = 4, column=4,pady=1)

btne = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.euler, text = "e", bg="grey58").grid(row = 5, column=4,pady=1)

btnlog = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, command=valor_adicionado.log, text = "log", bg="grey58").grid(row = 1, column=5,pady=1)

btnlog2 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "log2",command=valor_adicionado.log2, bg="grey58").grid(row = 2, column=5,pady=1)

btnlog10 = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "log10",command=valor_adicionado.log10, bg="grey58").grid(row = 3, column=5,pady=1)

btnquad = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4,command=valor_adicionado.quad, text = "^2", bg="grey58").grid(row = 4, column=5,pady=1)

btnexpo = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "exp",command=valor_adicionado.exp, bg="grey58").grid(row = 5, column=5,pady=1)

btninte = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "∫", bg="grey58").grid(row = 0, column=6,pady=1)

btnderiv = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "dy/dx", bg="grey58").grid(row = 1, column=6,pady=1)

btnlim = Button(calculo, width=6, height=2, font=("arial", 20, "bold"),fg="white", bd=4, text = "lim", bg="grey58").grid(row = 2, column=6,pady=1)
#====================================================MENU=============================================================


def saida():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica","Deseja sair?")#abre uma caixa com a msg escrita
    if sair > 0:
        root.destroy()
        return

def cientifica():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("832x568+450+90")

def padrao():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("718x568+450+90")

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
