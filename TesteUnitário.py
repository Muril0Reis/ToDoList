import unittest
from datetime import datetime
from ToDoList import Tarefa, ListaDeTarefas

class TestListaDeTarefas(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste, criando uma nova lista de tarefas"""
        self.lista_tarefas = ListaDeTarefas()

    def test_adicionar_tarefa(self):
        """Testa a adição de uma tarefa"""
        titulo = "Tarefa 1"
        self.lista_tarefas.adicionar_tarefa(titulo)
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa.titulo, titulo)

    def test_marcar_tarefa_como_concluida(self):
        """Testa marcar uma tarefa como concluída"""
        titulo = "Tarefa 2"
        self.lista_tarefas.adicionar_tarefa(titulo)
        self.lista_tarefas.marcar_tarefa_como_concluida(titulo)
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertTrue(tarefa.concluida)

    def test_editar_tarefa(self):
        """Testa a edição de uma tarefa"""
        titulo_antigo = "Tarefa 3"
        titulo_novo = "Tarefa 3 Editada"
        self.lista_tarefas.adicionar_tarefa(titulo_antigo)
        self.lista_tarefas.editar_tarefa(titulo_antigo, titulo_novo)
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo_novo)
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa.titulo, titulo_novo)

    def test_remover_tarefa(self):
        """Testa a remoção de uma tarefa"""
        titulo = "Tarefa 4"
        self.lista_tarefas.adicionar_tarefa(titulo)
        self.lista_tarefas.remover_tarefa(titulo)
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNone(tarefa)

    def test_encontrar_tarefa_por_titulo(self):
        """Testa a busca de uma tarefa pelo título"""
        titulo = "Tarefa 5"
        self.lista_tarefas.adicionar_tarefa(titulo)
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertEqual(tarefa.titulo, titulo)

    def test_marcar_tarefa_inexistente_como_concluida(self):
        """Testa a marcação de tarefa inexistente como concluída"""
        titulo = "Tarefa Inexistente"
        self.lista_tarefas.marcar_tarefa_como_concluida(titulo)

if __name__ == "__main__":
    unittest.main()
