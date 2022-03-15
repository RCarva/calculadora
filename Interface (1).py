from tkinter.ttk import *
import tkinter.messagebox


class Interface:
    def __init__(self, display, operacoes_elementares, derivada, limite):
        self.limite = limite
        self.derivada = derivada
        self.valor_adicionado = operacoes_elementares
        self.Display = display
        self.numberpadkk = "789456123"

    def config_button(self):
        btn = []
        i = 0
        for j in range(2, 5):
            for k in range(3):
                btn.append(Button(self.Display.aba1, width=6, text=self.numberpadkk[i]))
                btn[i].grid(row=j, column=k, pady=1)
                btn[i]["command"] = lambda x=self.numberpadkk[i]: self.valor_adicionado.num_entrada(x)
                i += 1
        self.btnlimpar = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.limpar(), text=chr(67)).grid(row=1, column=0, pady=1)

        self.btnlimptudo = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.limpar_tudo(), text=chr(67) + chr(69)).grid(row=1, column=1, pady=1)

        self.btnraiz = Button(self.Display.aba1, width=6, command=self.valor_adicionado.raiz, text="√").grid(row=1, column=2, pady=1)

        self.btnsoma = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.operação("+"), text="+").grid(row=1, column=3, pady=1)

        self.btnsubt = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.operação("-"), text="-").grid(row=2, column=3, pady=2)

        self.btnmult = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.operação("*"), text="*").grid(row=3, column=3, pady=3)

        self.btndiv = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.operação("/"), text=":").grid(row=4, column=3, pady=4)

        self.btnquad = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.quad(), text="^2").grid(row=5, column=0, pady=1)

        self.btnzero = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.num_entrada(0), text="0").grid(row=5, column=1, pady=1)

        self.btnponto = Button(self.Display.aba1, width=6, command=lambda: self.valor_adicionado.num_entrada("."), text=".").grid(row=5, column=2, pady=1)

        self.btnigual = Button(self.Display.aba1, width=6, command=lambda: [self.valor_adicionado.somatório()], text="=").grid(row=5, column=3, pady=1)

        # ============================================CALC-CIENTIFICA==========================================================

        # botoes calc cientifica

        self.btnpi = Button(self.Display.aba1, width=6, command=self.valor_adicionado.pi, text="π").grid(row=1, column=4, pady=1)

        self.btnsen = Button(self.Display.aba1, width=6, command=self.valor_adicionado.seno, text="sen").grid(row=2, column=4, pady=1)

        self.btncos = Button(self.Display.aba1, width=6, command=self.valor_adicionado.cos, text="cos").grid(row=3, column=4, pady=1)

        self.btntg = Button(self.Display.aba1, width=6, command=self.valor_adicionado.tan, text="tg").grid(row=4, column=4, pady=1)

        self.btne = Button(self.Display.aba1, width=6, command=self.valor_adicionado.euler, text="e").grid(row=5, column=4, pady=1)

        self.btnlog = Button(self.Display.aba1, width=6, command=self.valor_adicionado.log, text="log").grid(row=1, column=5, pady=1)

        self.btnlog2 = Button(self.Display.aba1, width=6, text="log2",
                              command=self.valor_adicionado.log2).grid(row=2, column=5, pady=1)

        self.btnlog10 = Button(self.Display.aba1, width=6, text="log10",
                               command=self.valor_adicionado.log10).grid(row=3, column=5, pady=1)

        self.btnloglp = Button(self.Display.aba1, width=6, command=self.valor_adicionado.log1p, text="ln").grid(row=4, column=5, pady=1)

        self.btnexpo = Button(self.Display.aba1, width=6, text="exp",
                              command=self.valor_adicionado.exp).grid(row=5, column=5, pady=1)

        self.btna = Button(self.Display.aba1, width=6, text="a", command=self.limite.abrir_janela_a).grid(row=0, column=6, pady=1)

        self.btnc = Button(self.Display.aba1, width=6, text="c").grid(row=1, column=6, pady=1)

        self.btnd = Button(self.Display.aba1, width=6, text="d").grid(row=2, column=6, pady=1)

        self.btnderiv = Button(self.Display.aba1, width=6, text="dy/dx",
                               command=self.derivada.abrir_janela_derivada).grid(row=4, column=6, pady=1)

        self.btnlim = Button(self.Display.aba1, width=6, text="lim", command=self.limite.abrir_janela_limite).grid(row=5, column=6, pady=1)

        self.btninte = Button(self.Display.aba1, width=6, text="∫").grid(row=3, column=6, pady=1)

    # ====================================================Aba Ver Ajuda=====================================================================================================
    def config_labels(self):
        self.labels1 = Label(self.Display.aba2, text="Cálculos possiveis:\n> Aritiméticos\n> Funções\n> Valor das Constantes",
                        font=("Arial", 10), borderwidth=2, relief="flat").pack(side= tkinter.LEFT)
        self.labels2 = Label(self.Display.aba2,
                             text="""Informações sobre Limites:\n> O botão 'a' recebe o valor ao qual x deve tender.
                             \n> Para realizar o cálculo, basta definir um valor para 'a', apertar o botão 'lim' e digitar sua função.
                             \n> As funções devem ser digitadas com a síntaxe do python, em especial, deve-se usar '**' para exponenciação.""",
                             font=("Arial", 10), borderwidth=2, relief="flat").pack(side= tkinter.LEFT)
        self.labels3 = Label(self.Display.aba2,
                        text="""Informações sobre Derivadas:\n> Para realizar o cálculo, basta apertar o botão dy/dx e digitar sua função.
                        \n> As funções devem ser digitadas com a síntaxe do python, em especial, deve-se usar '**' para exponenciação.""",
                        font=("Arial", 10), borderwidth=2, relief="flat").pack(side= tkinter.TOP)

    # ===================================================Aba Historico======================================================================================================
    def config_historico(self):
        arquivo = open(self.Display.caminho + "/Contas da Calculadora.txt", "r")
        historico = arquivo.readlines()
        listbox_widget = tkinter.Listbox(self.Display.aba3)
        for entry in historico:
            listbox_widget.insert(tkinter.END, entry)
        listbox_widget.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
        arquivo.close()

    # ====================================================MENU==============================================================================================================

    #def saida():
        #sair = tkinter.messagebox.askyesno("Calculadora Cientifica", "Deseja sair?")  # abre uma caixa com a msg escrita
        #if sair > 0:
            #Interface.root.destroy()
            #return
    #def config_menubar(self):
        #self.menubar = Menu(Display.aba1)
        #self.padraomenu = Menu(menubar, tearoff=0)
    #menubar.add_cascade(label="Sair", command=saida)  # adiciona a opcao do usuario clicar em "opções"

    #Display.root.config(menu=menubar)
    #Display.root.mainloop()
