import math
from tkinter import *

class Operações_Elementares():  # Vai cuidar de todas as operações mais simples e conversões
    def __init__(self, display):
        self.Display = display
        self.total = 0
        self.atual = ''
        self.valor = True
        self.chk_soma = False
        self.op = ''
        self.resultado = False

    def display(self, value):  # Controla o que está sendo demonstrado
        self.Display.entrada.delete(0, END)
        self.Display.entrada.insert(0, value)

    def num_entrada(self, num):  # Modifica os números na Display.entrada para contas rápidas
        self.resultado = False
        num1 = self.Display.entrada.get()
        num2 = str(num)
        if self.valor:
            self.atual = num2
            self.valor = False
        else:
            if num2 == '.':
                if num2 in num1:
                    return
            self.atual = num1 + num2
        self.display(self.atual)
        self.Display.persistencia(num)

    def operação(self, op):  # Chama as operações se baseando nos botões
        self.atual = float(self.atual)
        if self.chk_soma:
            self.função()
        elif not self.resultado:
            self.total = self.atual
            self.valor = True
        self.chk_soma = True
        self.op = op
        self.resultado = False
        self.Display.persistencia(self.op)

    def somatório(self):  # Faz o uso de diferentes entradas
        self.resultado = True
        self.atual = float(self.atual)
        if self.chk_soma == True:
            self.função()
        else:
            self.total = float(self.Display.entrada.get())

    def função(self):  # Faz as operações se baseando nos botões com os comandos atrelados
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
        self.valor = True
        self.chk_soma = False
        self.display(self.total)
        self.Display.persistencia(" = ")
        self.Display.persistencia(float(self.total))
        self.Display.persistencia("\n")
        # Display.close()
        # Display.open()

    def limpar(self):  # Função que limpa o display
        self.resultado = False
        self.atual = "0"
        self.display(0)
        self.valor = True
        self.Display.persistencia("\n")
        self.Display.persistencia("Limpar")
        self.Display.persistencia("\n")
        self.Display.persistencia(str(self.total) + self.op)

    def limpar_tudo(self):  # Função que limpa as funções
        self.resultado = False
        self.atual = "0"
        self.display(0)
        self.valor = True
        self.total = 0
        # Display.persistencia("\n")
        self.Display.persistencia("Limpar Tudo")
        self.Display.persistencia("\n")

    # ==========================================================================Conversões Rápidas==========================================================================

    def pi(self):  # Converte π
        self.resultado = False
        self.atual = math.pi
        self.display(self.atual)
        self.Display.persistencia(self.atual)
        self.Display.persistencia("\n")

    def euler(self):  # Converte e
        self.resultado = False
        self.atual = math.e
        self.display(self.atual)
        self.Display.persistencia(self.atual)
        self.Display.persistencia("\n")

    def raiz(self):  # Faz a raiz do número no resultado
        self.resultado = False
        self.atual = math.sqrt(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia("^1/2 = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def cos(self):  # Faz o Coseno do número no resultado
        self.resultado = False
        self.atual = math.cos(math.radians(float(self.Display.entrada.get())))
        self.display(self.atual)
        self.Display.persistencia(" cos = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def tan(self):  # Faz a Tangente do número no resultado
        self.resultado = False
        self.atual = math.tan(math.radians(float(self.Display.entrada.get())))
        self.display(self.atual)
        self.Display.persistencia(" tan = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def seno(self):  # Faz o Seno do número no resultado
        self.resultado = False
        self.atual = math.sin(math.radians(float(self.Display.entrada.get())))
        self.display(self.atual)
        self.Display.persistencia(" sen = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def log(self):  # Faz o Log do número no resultado
        self.resultado = False
        self.atual = math.log(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia(" = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def exp(self):  # Faz o Exponencial na base e do número no resultado
        self.resultado = False
        self.atual = math.exp(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia(" = ln(")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia(")\n")

    def quad(self):  # Converte radianos em graus do número no resultado
        self.resultado = False
        self.atual = math.pow(float(self.Display.entrada.get()), 2)
        self.display(self.atual)
        self.Display.persistencia("^2 = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def log2(self):  # Faz o Log de base 2 do número no resultado
        self.resultado = False
        self.atual = math.log2(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia(" = 2^")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def log10(self):  # Faz o Log de base 10 do número no resultado
        self.resultado = False
        self.atual = math.log10(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia(" = 10^")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")

    def log1p(self):  # Faz o Log na base e de 1+ o número no resultado
        self.resultado = False
        self.atual = math.log1p(float(self.Display.entrada.get()))
        self.display(self.atual)
        self.Display.persistencia(" = ")
        self.Display.persistencia(float(self.atual))
        self.Display.persistencia("\n")
