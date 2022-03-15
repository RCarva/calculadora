from sympy import *
from tkinter.messagebox import showinfo
from tkinter import StringVar, Toplevel, Entry, Label, Button


class Derivada():
    def __init__(self, display):
        self.Display = display
        self.equacao = StringVar()
        self.x = symbols('x') # transforma a string 'x' em um simbolo matematico
        self.derivada = 0

    def abrir_janela_derivada(self):
        self.nova_janela = Toplevel(self.Display.root)
        self.nova_janela.title('Calcula Derivada')
        self.nova_janela.geometry('300x150')
        self.nova_janela.resizable(False, False)
        self.nova_janela_entrada = Entry(self.nova_janela, textvariable=self.equacao)
        self.nova_janela_entrada.pack(fill='x', expand=True)
        self.nova_janela_entrada.focus()
        self.nova_janela_label = Label(self.nova_janela, text='Digite sua função:')
        self.nova_janela_label.pack(fill='x', expand=True)
        self.calc_button = Button(self.nova_janela, text='Calcula', command=self.calcula_derivada)
        self.calc_button.pack(fill='x', expand=True, pady=10)

    def calcula_derivada(self): # calcula a derivada
        self.equacao = sympify(self.nova_janela_entrada.get())
        self.derivada = diff(self.equacao, self.x)
        showinfo(message=str(self.derivada))
        self.Display.persistencia('\n')
        self.Display.persistencia('dy/dx(')
        self.Display.persistencia(self.equacao)
        self.Display.persistencia(')')
        self.Display.persistencia('=')
        self.Display.persistencia(self.derivada)