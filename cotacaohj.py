from tkinter import Button, Label
from tkinter.tix import Tk
import requests
def pegar_cotacoes(): 
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar =  requisicao_dic['USDBRL']['bid']
    cotacao_euro =  requisicao_dic['EURBRL']['bid']
    cotacao_btc =  requisicao_dic['BTCBRL']['bid']

    texto =  f'''
    Dolar: R$ {cotacao_dolar}
    Euro: R$ {cotacao_euro}
    Bitcoin: R$ {cotacao_btc}'''

    texto_resposta["text"]=texto


janela = Tk() 
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações dea moedas, Dolar - Euro - Bitcoin")
texto.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=20, pady=20)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=20, pady=20)


janela.mainloop()


