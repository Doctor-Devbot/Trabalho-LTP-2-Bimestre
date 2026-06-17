from model.jogador import Jogador
from model.resposta import Resposta
from model.atividade import Atividade
from model.lista_atividade import ListaAtividade
from model.modulo import Modulo
from model.comando import Comando

# Jogador
jogador = Jogador("Gabriel", "gabriel@email.com")
print(jogador)

jogador.set_nome("Gabriel Alves")
jogador.set_email("gabrielalves@email.com")

print(jogador.get_nome())
print(jogador.get_email())

# Resposta
resposta = Resposta(True)
print(resposta)

resposta.set_correta(False)
print(resposta.get_correta())

# Atividade
atividade = Atividade(
    1,
    "Qual comando SQL seleciona dados?",
    ["SELECT", "INSERT", "DELETE", "UPDATE"],
    jogador,
    resposta
)

print(atividade)

print(atividade.get_id())
print(atividade.get_enunciado())
print(atividade.get_alternativas())
print(atividade.get_jogador())
print(atividade.get_resposta())

atividade.set_enunciado("Novo enunciado")
atividade.set_alternativas(["A", "B", "C", "D"])

print(atividade)

# Lista de Atividades
lista = ListaAtividade(
    "Consultas SQL",
    "Lista de exercícios sobre SQL"
)

lista.atividades.append(atividade)

print(lista)
print(lista.get_titulo())
print(lista.get_descricao())

# Módulo
modulo = Modulo(
    "Banco de Dados",
    "Módulo introdutório"
)

modulo.listas_atividade.append(lista)

print(modulo)
print(modulo.get_titulo())
print(modulo.get_descricao())

# Comando
comando = Comando(
    "SELECT",
    "Seleciona registros de uma tabela"
)

print(comando)

print(comando.get_titulo())
print(comando.get_descricao())

comando.set_titulo("SELECT DISTINCT")
comando.set_descricao("Seleciona registros sem repetição")

print(comando)

# Teste do to_dic
print("\nDicionário da atividade:")
print(atividade.to_dic())

print("\nDicionário do jogador:")
print(jogador.to_dic())

# Teste das validações
print("\nTestando validações:")

try:
    jogador.set_email("emailinvalido")
except ValueError as e:
    print("Erro:", e)

try:
    atividade.set_enunciado("")
except ValueError as e:
    print("Erro:", e)

try:
    atividade.set_id(-1)
except ValueError as e:
    print("Erro:", e)