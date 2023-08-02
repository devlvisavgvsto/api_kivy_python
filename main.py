import requests
import locale
from kivy.app import App
from kivy.lang import Builder

locale.setlocale(locale.LC_ALL, 'pt_BR')

GUI = Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return GUI

    def on_start(self):
        try:
            cotacao_bitcoin = self.cotacao("BTC")
            alta_bitcoin = self.alta_da_moeda("BTC")
            formatted_cotacao = locale.format_string("%.2f", cotacao_bitcoin, grouping=True)
            formatted_alta = locale.format_string("%.2f", alta_bitcoin, grouping=True)
            self.root.ids["moeda1"].text = f"Bitcoin R$ {formatted_cotacao}"
            self.root.ids["alta"].text = f'Valor Max diário || R$ {formatted_alta}'
        except Exception as e:
            print(f"Erro: {e}")
            self.root.ids["moeda1"].text = "Erro ao obter a cotação"
            self.root.ids["alta"].text = "Erro ao obter a alta"

    def cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return float(cotacao)

    def alta_da_moeda(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        alta_da_moeda = dic_requisicao[f"{moeda}BRL"]["high"]
        return float(alta_da_moeda)

MyApp().run()

