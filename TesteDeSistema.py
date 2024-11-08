import unittest
from ToDoList import ListaDeTarefas


class TesteSistemaListaDeTarefas(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste"""
        self.lista_tarefas = ListaDeTarefas()

    def test_sistema_completo(self):
        """Testa todas as operações do sistema"""
        titulo_adicionar = "Tarefa para Sistema"
        # Adicionando uma tarefa
        self.lista_tarefas.adicionar_tarefa(titulo_adicionar)
        tarefa_adicionada = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo_adicionar)
        self.assertIsNotNone(tarefa_adicionada)

        # Editando a tarefa
        novo_titulo = "Tarefa Sistema Editada"
        self.lista_tarefas.editar_tarefa(titulo_adicionar, novo_titulo)
        tarefa_editada = self.lista_tarefas.encontrar_tarefa_por_titulo(novo_titulo)
        self.assertEqual(tarefa_editada.titulo, novo_titulo)

        # Marca a tarefa como concluída
        self.lista_tarefas.marcar_tarefa_como_concluida(novo_titulo)
        self.assertTrue(tarefa_editada.concluida)

        # Removendo a tarefa
        self.lista_tarefas.remover_tarefa(novo_titulo)
        tarefa_removida = self.lista_tarefas.encontrar_tarefa_por_titulo(novo_titulo)
        self.assertIsNone(tarefa_removida)
