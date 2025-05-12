import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()


def chamaPopup():    
    iteracoes = simpledialog.askinteger("Número de Rodadas", "Digite o número de rodadas:",  parent=ROOT, minvalue=1, maxvalue=100000)
    if iteracoes is None: # Usuário cancelou ou fechou a caixa de diálogo
        print("Nenhum número de rodadas fornecido. Saindo.")
        exit()
    else:
        return iteracoes

iteracoes = chamaPopup()

