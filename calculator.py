import math
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Calculadora Cientifica")
root.configure(background ="black") #referente a cor da calculadora 
root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
root.geometry("800x600+0+0")#695x568 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior



nb = ttk.Notebook(root)
nb.place(x=0, y=0, width=800, height=800)
aba1 = Frame(nb)
nb.add(aba1, text="calculadora cientifica")
aba2 = Frame(nb)
nb.add(aba2, text="Ver Ajuda")
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
    
    def par(self):
        self.resultado=False
        self.atual = 0
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

#===================================================Contas Calculadora Cientifica======================================


"""def CalculadoraCientifica(sinal):
    if sinal == "c":
        del lista[-1]

    if sinal == "ci":
        lista = list
    
    if sinal == "x":
        if len(lista) != 0:
            lista[-1].setX = True
        else:
            lista.append(Keyboard("1"))
            lista[-1].setX = True
     
    if sinal not in "cix":
        lista.append(Keyboard(sinal))

    
    a =  Derivada(lista)
    visor = a.visorEquacao()

    if sinal == "=" and lista[0].str == "dx":
        del a[0]
        a =  Derivada(lista)
        a.potencia()
        a.contaDerivada()
        visor = a.str


    if sinal == "=" and lista[0].str == "lim":
        del a[0]
        a.Lim(lista)

    return visor"""

#====================================================Interface grafica================================================

abas = [aba1]

#botoes calc simples 
for aba in abas:
    if aba == aba1:

        entrada = Entry(aba, font = ("arial",20,"bold"), bg="white", bd=30, width=40,justify=RIGHT)
        entrada.grid(row = 0, column=0, columnspan=6,pady=1)
        entrada.insert(0,"0")

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

#====================================================Aba Ver Ajuda=====================================================================================================

ttk.Label(aba2,text="Tipos de Calculos que podem ser feitos:\n> Aritiméticos\n> Funções\n> Valor das Constantes\n\n",font="Helvetica").grid(column=1, row=2)
ttk.Label(aba2,text="Casos de Limites:\n> bla\n> bla\n> bla",font="Helvetica\n\n").grid(column=2, row=2)
ttk.Label(aba2,text="Casos de Derivadas:\n> loll\n> lol \n> bla",font="Helvetica").grid(column=3, row=2)

#====================================================MENU==============================================================================================================


def saida():
    sair = tkinter.messagebox.askyesno("Calculadora Cientifica","Deseja sair?")#abre uma caixa com a msg escrita
    if sair > 0:
        root.destroy()
        return

"""def cientifica():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("812x568+450+90")

def padrao():
    root.resizable(width=False, height= False)#Usuário n pode alterar as dimensoes
    root.geometry("695x568+450+90")"""

menubar = Menu(aba1)
padraomenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Sair" , command=saida)#adiciona a opcao do usuario clicar em "opções"
#padraomenu.add_command(label = "Calculadora Padrão", command= padrao)
#padraomenu.add_command(label = "Calculadora científica", command= cientifica)
#padraomenu.add_separator()
#padraomenu.add_command(label = "Sair", command= saida)


root.config(menu = menubar)
root.mainloop()
