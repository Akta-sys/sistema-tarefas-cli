from tarefas.models import Tarefa
from tarefas.storage import carregar_tarefas, salvar_tarefas

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. [{t['status']}] {t['titulo']} (Prioridade: {t['prioridade']})")

def adicionar_tarefa():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Piroridade (baixa/media/alta): ")
    nova = Tarefa(titulo, descricao, prioridade)
    tarefas = carregar_tarefas()
    tarefas.append(nova.to_dict())
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    tarefas = carregar_tarefas()
    listar_tarefas()
    idx = int(input("Número da tarefa para remover: ")) - 1
    if 0 <= idx < len(tarefas):
        del tarefas[idx]
        salvar_tarefas(tarefas)
        print("Tarefa removida.")
    else:
        print("Índice inválido.")

def menu_principal():
    while True:
        print("\n=== MENU ===")
        print("1. Listar tarefa")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")