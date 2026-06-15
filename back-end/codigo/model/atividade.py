class Atividade:
    def __init__(self, id_atividade, enunciado, jogador=None, resposta=None):
        self.id_atividade = id_atividade
        self.enunciado = enunciado
        self.jogador = jogador
        self.resposta = resposta

    def get_enunciado(self):
        return self.enunciado

    def set_enunciado(self, enunciado):
        self.enunciado = enunciado

    def get_id(self):
        return self.id_atividade

    def set_id(self, id_atividade):
        self.id_atividade = id_atividade

    def to_dic(self):
        return {
            "id_atividade": self.id_atividade,
            "enunciado": self.enunciado
        }

    #def gerar_questão()
        