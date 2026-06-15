from model.atividade import Atividade

class AtividadeDAO:
    def __init__(self):
        self._database = [
            Atividade(1, "Escreva uma consulta SQL que liste todos os clientes cadastrados."),
            Atividade(2, "Crie uma consulta SQL utilizando WHERE para mostrar apenas os produtos com preço maior que 100.")
        ]
    
    def create(self, id_atividade, enunciado):
        existente = next((a for a in self._database if a.id_atividade == id_atividade), None)
        if existente:
            return None
        atividade = Atividade(id_atividade, enunciado)
        self._database.append(atividade)
        return atividade.to_dic()
   
    def update_enunciado(self, id_atividade, enunciado):
        atividade = next((a for a in self._database if a.id_atividade == id_atividade), None)
        if atividade:
            atividade.enunciado = enunciado
            return atividade.to_dic()
        return None

    def retrieve_by_id(self, id_atividade):
        atividade = next((a for a in self._database if a.id_atividade == id_atividade),None)
        if atividade:
            return atividade.to_dic()
        return None
    
    def retrieve_all(self):
        return [a.to_dic() for a in self._database]
    
    def delete(self, id_atividade):
        atividade = next((a for a in self._database if a.id_atividade == id_atividade), None)
        if atividade:
            self._database.remove(atividade)
            return atividade.to_dic()
        return None

    def size(self):
        return len(self._database)



