# importar o App, Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build
# # pegar: DÓLAR US, EURO, LIBRA ESTERLINA, DÓLAR CANADÁ, IENE, Won Norte-Coreano, Yuan Chinês, Rublo
# # BITCOIN, ETHEREUM,

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda001"].text = f"DÓLAR (USA) \nR${self.pegar_cotacao('USD')}"
        self.root.ids["moeda002"].text = f"EURO \nR${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda003"].text = f"LIBRA ESTERLINA (UK) \nR${self.pegar_cotacao('GBP')}"
        self.root.ids["moeda004"].text = f"DÓLAR (CAD) \nR${self.pegar_cotacao('CAD')}"
        self.root.ids["moeda005"].text = f"IENE JAPONÊS \nR${self.pegar_cotacao('JPY')}"
        self.root.ids[
            "moeda006"].text = f"GUARANI PARAGUAIO \nR${self.pegar_cotacao('PYG')}"
        self.root.ids["moeda007"].text = f"YUAN (CHINA) \nR${self.pegar_cotacao('CNY')}"
        self.root.ids["moeda008"].text = f"RUBLO (RUSSIA) \nR${self.pegar_cotacao('RUB')}"
        self.root.ids["moeda009"].text = f"BITCOIN \nR${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda0010"].text = f"ETHEREUM \nR${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
