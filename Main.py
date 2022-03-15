from Display import Display
from OperacoesElementares import Operações_Elementares
from Interface import Interface
from derivada import Derivada
from limite import Limite


calculadora = Display()
calculadora.config_root()
calculadora.config_notebook()
calculadora.config_entrada()

valor_adicionado = Operações_Elementares(calculadora)
derivada = Derivada(calculadora)
limite = Limite(calculadora)


interface = Interface(calculadora, valor_adicionado, derivada, limite)
interface.config_button()
interface.config_labels()
interface.config_historico()


calculadora.root.mainloop()