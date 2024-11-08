from ToDoList import ListaDeTarefas
from datetime import datetime

def exibir_menu():
    print("\nMenu de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Editar Tarefa")
    print("5. Remover Tarefa")
    print("6. Sair")

def main():
    lista_tarefas = ListaDeTarefas()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título da tarefa: ")
            data_texto = input("Digite a data de vencimento (YYYY-MM-DD) ou deixe em branco: ")
            data_vencimento = datetime.strptime(data_texto, "%Y-%m-%d") if data_texto else None
            lista_tarefas.adicionar_tarefa(titulo, data_vencimento)
            print("Tarefa adicionada com sucesso!")

        elif escolha == "2":
            print("\nTarefas:")
            print(lista_tarefas.listar_tarefas())

        elif escolha == "3":
            titulo = input("Digite o título da tarefa a marcar como concluída: ")
            lista_tarefas.marcar_tarefa_como_concluida(titulo)

        elif escolha == "4":
            titulo = input("Digite o título da tarefa a editar: ")
            novo_titulo = input("Digite o novo título: ")
            nova_data_texto = input("Digite a nova data de vencimento (YYYY-MM-DD) ou deixe em branco: ")
            nova_data_vencimento = datetime.strptime(nova_data_texto, "%Y-%m-%d") if nova_data_texto else None
            lista_tarefas.editar_tarefa(titulo, novo_titulo, nova_data_vencimento)

        elif escolha == "5":
            titulo = input("Digite o título da tarefa a remover: ")
            lista_tarefas.remover_tarefa(titulo)

        elif escolha == "6":
            print("Saindo do aplicativo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()