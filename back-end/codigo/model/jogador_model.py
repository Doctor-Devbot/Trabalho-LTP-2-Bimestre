class jogadorModel:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def get_nome(self):
        return self.nome
    def get_email(self):
        return self.email
    def set_nome(self, nome):
        self.nome = nome
        return self.nome
    def set_email(self, email):
        self.email = email
        return self.email