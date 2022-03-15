from sympy import *
from tkinter.messagebox import showinfo
from tkinter import StringVar, Toplevel, Entry, Label, Button


class Limite():
    def __init__(self, display):
        self.Display = display
        self.equacao = StringVar()
        self.a = StringVar()
        self.x = symbols('x')  # transforma a string 'x' em um simbolo matematico
        self.limite = 0

    def abrir_janela_a(self):
        self.nova_janela_a = Toplevel(self.Display.root)
        self.nova_janela_a.title('Define a')
        self.nova_janela_a.geometry('300x150')
        self.nova_janela_a.resizable(False, False)
        self.nova_janela_a_entrada = Entry(self.nova_janela_a, textvariable=self.a)
        self.nova_janela_a_entrada.pack(fill='x', expand=True)
        self.nova_janela_a_entrada.focus()
        self.nova_janela_a_label = Label(self.nova_janela_a, text='Digite o valor de a:')
        self.nova_janela_a_label.pack(fill='x', expand=True)
        self.calc_button_a = Button(self.nova_janela_a, text='Ok!', command=self.set_a)
        self.calc_button_a.pack(fill='x', expand=True, pady=10)

    def abrir_janela_limite(self):
        self.nova_janela = Toplevel(self.Display.root)
        self.nova_janela.title('Calcula Limite')
        self.nova_janela.geometry('300x150')
        self.nova_janela.resizable(False, False)
        self.nova_janela_entrada = Entry(self.nova_janela, textvariable=self.equacao)
        self.nova_janela_entrada.pack(fill='x', expand=True)
        self.nova_janela_entrada.focus()
        self.nova_janela_label = Label(self.nova_janela, text='Digite sua função:')
        self.nova_janela_label.pack(fill='x', expand=True)
        self.calc_button = Button(self.nova_janela, text='Calcula', command=self.calcula_limite)
        self.calc_button.pack(fill='x', expand=True, pady=10)

    def set_a(self):
        self.a = sympify(self.nova_janela_a_entrada.get())
        showinfo(message='a='+str(self.a))

    def calcula_limite(self): # calcula o limite
        self.equacao = sympify(self.nova_janela_entrada.get())
        self.limite = limit(self.equacao, self.x, self.a)
        showinfo(message=str(self.limite))
        self.Display.persistencia('\n')
        self.Display.persistencia('lim x->{}('.format(self.a))
        self.Display.persistencia(self.equacao)
        self.Display.persistencia(')')
        self.Display.persistencia('=')
        self.Display.persistencia(self.limite)





