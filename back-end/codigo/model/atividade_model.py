from jogador_model import JogadorModel
from resposta_model import RespostaModel
class AtividadeModel:
    def __init__(self, enunciado):
        self.enunciado = enunciado
        self.jogador = JogadorModel
        self.resposta = RespostaModel
    def get_enunciado(self):
        return self.enunciado
    def set_enunciado(self, enunciado):
        self.enunciado = enunciado

    #def gerar_questão()
        