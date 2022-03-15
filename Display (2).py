from tkinter import *
from tkinter import ttk
import os


class Display():  # Traduz as letras e símbolos e grava no arquivo de histórico

    def __init__(self):
        self.root = Tk()
        self.file = open("Contas da Calculadora.txt", "a+")
        self.nb = ttk.Notebook(self.root)
        self.caminho = os.getcwd()
        self.equacao = StringVar()

    def config_root(self):
        self.root.title("Calculadora Cientifica")
        self.root.configure(background="black")  # referente a cor da calculadora
        self.root.resizable(width=False, height=False)  # Usuário n pode alterar as dimensoes
        self.root.geometry("800x300+0+0")  # 800X600 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior


    def config_notebook(self):
        self.nb.place(x=0, y=0, width=800, height=800)  # tamanho das abas
        self.aba1 = Frame(self.nb)
        self.nb.add(self.aba1, text="Calculadora científica")
        self.aba2 = Frame(self.nb)
        self.nb.add(self.aba2, text="Ver ajuda")
        self.aba3 = Frame(self.nb)
        self.nb.add(self.aba3, text="Histórico")

    def persistencia(self, dado):  # Abre um arquivo txt e grava o dado no arquivo
        with open(self.caminho + "/Contas da Calculadora.txt", "a") as log:
            dado = str(dado)
            log.writelines(dado)

    def config_entrada(self):
        self.entrada = Entry(self.aba1, textvariable=self.equacao, font=("arial", 20, "bold"), bg="white", bd=30, width=40, justify=RIGHT)
        self.entrada.grid(row=0, column=0, columnspan=6, pady=1)
        self.entrada.insert(0, "")



    # caminho = os.getcwd()
    # root = Tk()
    # root.title("Calculadora Cientifica")
    # root.configure(background="black")  # referente a cor da calculadora
    # root.resizable(width=False, height=False)  # Usuário n pode alterar as dimensoes
    # root.geometry("800x600+0+0")  # 800X600 sao as dimensoes. O +0+0 significa q o programa vai iniciar suas dimencoes na direita superior
    # file = open("Contas da Calculadora.txt", "a+")
    # nb = ttk.Notebook(root)  # Criação de abas
    # nb.place(x=0, y=0, width=800, height=800)  # tamanho das abas
    # aba1 = Frame(nb)
    # nb.add(aba1, text="Calculadora científica")
    # aba2 = Frame(nb)
    # nb.add(aba2, text="Ver ajuda")
    # aba3 = Frame(nb)
    # nb.add(aba3, text="Histórico")

    # def abrir_janela1(self):
    # nova_janela = TopLevel()
