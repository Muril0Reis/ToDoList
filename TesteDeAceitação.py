import unittest
from ToDoList import ListaDeTarefas

class TesteDeAceitacao(unittest.TestCase):
    def setUp(self):
        """Configura um ambiente limpo para cada teste de aceitação."""
        self.lista_tarefas = ListaDeTarefas()
    
    def test_fluxo_de_usuario(self):
        # Adicionar tarefa
        self.lista_tarefas.adicionar_tarefa("Estudar para a prova")
        self.assertEqual(len(self.lista_tarefas.tarefas), 1, "Erro ao adicionar tarefa")

        # Marcar tarefa como concluída
        self.lista_tarefas.marcar_tarefa_como_concluida("Estudar para a prova")
        self.assertTrue(self.lista_tarefas.tarefas[0].concluida, "Erro ao marcar tarefa como concluída")

        # Editar tarefa
        self.lista_tarefas.editar_tarefa("Estudar para a prova", "Estudar para a prova de matemática")
        self.assertEqual(self.lista_tarefas.tarefas[0].titulo, "Estudar para a prova de matemática", "Erro ao editar tarefa")

        # Remover tarefa
        self.lista_tarefas.remover_tarefa("Estudar para a prova de matemática")
        self.assertEqual(len(self.lista_tarefas.tarefas), 0, "Erro ao remover tarefa")

if __name__ == '__main__':
    unittest.main()
