from model.atividade import Atividade

class AtividadeDAO:
    def __init__(self):
        self._database = [
            Atividade(1, "Qual comando SQL seleciona dados?", ["SELECT", "INSERT", "DELETE", "UPDATE"]),
            Atividade(2, "Qual cláusula filtra registros?", ["WHERE", "ORDER BY", "GROUP BY", "JOIN"])
        ]

    def create(self, id_atividade, enunciado, alternativas):
        existente = next((a for a in self._database if a.get_id() == id_atividade), None)
        if existente:
            return None
        atividade = Atividade(id_atividade, enunciado, alternativas)
        self._database.append(atividade)
        return atividade.to_dic()

    def update_enunciado(self, id_atividade, enunciado):
        atividade = next((a for a in self._database if a.get_id() == id_atividade), None)
        if atividade:
            atividade.set_enunciado(enunciado)
            return atividade.to_dic()
        return None

    def retrieve_by_id(self, id_atividade):
        atividade = next((a for a in self._database if a.get_id() == id_atividade), None)
        if atividade:
            return atividade.to_dic()
        return None

    def retrieve_all(self):
        return [a.to_dic() for a in self._database]

    def delete(self, id_atividade):
        atividade = next((a for a in self._database if a.get_id() == id_atividade), None)
        if atividade:
            self._database.remove(atividade)
            return atividade.to_dic()
        return None

    def size(self):
        return len(self._database)