from datetime import datetime

class Tarefa:
    def __init__(self, titulo, data_vencimento=None):
        self.titulo = titulo
        self.data_vencimento = data_vencimento
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def editar(self, novo_titulo, nova_data_vencimento=None):
        self.titulo = novo_titulo
        self.data_vencimento = nova_data_vencimento

    def __repr__(self):
        status = "✓" if self.concluida else "✗"
        return f"{self.titulo} - Vencimento: {self.data_vencimento} - Status: {status}"


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, data_vencimento=None):
        tarefa = Tarefa(titulo, data_vencimento)
        self.tarefas.append(tarefa)
        return tarefa

    def encontrar_tarefa_por_titulo(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa
        return None

    def marcar_tarefa_como_concluida(self, titulo):
        tarefa = self.encontrar_tarefa_por_titulo(titulo)
        if tarefa:
            tarefa.marcar_como_concluida()
            print(f"Tarefa '{titulo}' marcada como concluída.")
        else:
            print("Tarefa não encontrada.")

    def editar_tarefa(self, titulo, novo_titulo, nova_data_vencimento=None):
        tarefa = self.encontrar_tarefa_por_titulo(titulo)
        if tarefa:
            tarefa.editar(novo_titulo, nova_data_vencimento)
            print(f"Tarefa '{titulo}' foi editada.")
        else:
            print("Tarefa não encontrada.")

    def remover_tarefa(self, titulo):
        tarefa = self.encontrar_tarefa_por_titulo(titulo)
        if tarefa:
            self.tarefas.remove(tarefa)
            print(f"Tarefa '{titulo}' foi removida.")
        else:
            print("Tarefa não encontrada.")

    def listar_tarefas(self):
        return "\n".join(f"{i}. {tarefa}" for i, tarefa in enumerate(self.tarefas))
