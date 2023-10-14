class Time:
    def __init__(self, nome, cidade, mascote):
        self.nome = nome
        self.cidade = cidade
        self.mascote = mascote

class Jogador:
    def __init__(self, nome, time, numero_camisa):
        self.nome = nome
        self.time = time
        self.numero_camisa = numero_camisa

class ComissaoTecnica:
    def __init__(self, tecnico, auxiliar, preparador_fisico):
        self.tecnico = tecnico
        self.auxiliar = auxiliar
        self.preparador_fisico = preparador_fisico

times = []
jogadores = []
comissao = []

def cadastrar_time():
    nome = input("Nome do time: ")
    cidade = input("Cidade do time: ")
    mascote = input("Nome do mascote do time: ")
    time = Time(nome, cidade, mascote)
    times.append(time)

def cadastrar_jogador():
    nome = input("Nome do jogador: ")
    time_nome = input("Nome do time do jogador: ")
    numero_camisa = input("Número da camisa do jogador: ")
    jogador = Jogador(nome, time_nome, numero_camisa)
    jogadores.append(jogador)

def cadastrar_comissao():
    tecnico = input("Nome do técnico: ")
    auxiliar = input("Nome do auxiliar: ")
    preparador_fisico = input("Nome do preparador físico: ")
    comissao_tecnica = ComissaoTecnica(tecnico, auxiliar, preparador_fisico)
    comissao.append(comissao_tecnica)

while True:
    print("\nMenu:")
    print("1. Cadastrar time")
    print("2. Cadastrar jogador")
    print("3. Cadastrar comissão técnica")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_time()
    elif opcao == "2":
        cadastrar_jogador()
    elif opcao == "3":
        cadastrar_comissao()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Agora você pode acessar os dados cadastrados nas listas times, jogadores e comissao
