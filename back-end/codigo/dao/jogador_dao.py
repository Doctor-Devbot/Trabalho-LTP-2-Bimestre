from model.jogador import Jogador

class JogadorDAO:
    def __init__(self):
        self._database = [
            Jogador("Marco", "marco@gmail.com"),
            Jogador("Julia", "julia@gmail.com")
        ]

    def create(self, nome, email):
        existente = next((j for j in self._database if j.get_email() == email), None)
        if existente:
            return None
        jogador = Jogador(nome, email)
        self._database.append(jogador)
        return jogador.to_dic()

    def retrieve_by_email(self, email):
        jogador = next((j for j in self._database if j.get_email() == email), None)
        if jogador:
            return jogador.to_dic()
        return None

    def retrieve_all(self):
        return [j.to_dic() for j in self._database]

    def update_nome(self, email, nome):
        jogador = next((j for j in self._database if j.get_email() == email), None)
        if jogador:
            jogador.set_nome(nome)
            return jogador.to_dic()
        return None

    def delete(self, email):
        jogador = next((j for j in self._database if j.get_email() == email), None)
        if jogador:
            self._database.remove(jogador)
            return jogador.to_dic()
        return None

    def size(self):
        return len(self._database)