import unittest
from ToDoList import ListaDeTarefas


class TesteIntegracaoListaDeTarefas(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste"""
        self.lista_tarefas = ListaDeTarefas()

    def test_adicionar_e_editar_tarefa(self):
        """Testa a adição e edição de uma tarefa"""
        titulo = "Tarefa para Editar"
        self.lista_tarefas.adicionar_tarefa(titulo)
        # Verificando que a tarefa foi adicionada
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa.titulo, titulo)
        
        # Editando a tarefa
        novo_titulo = "Tarefa Editada"
        self.lista_tarefas.editar_tarefa(titulo, novo_titulo)
        # Verificando se a edição ocorreu corretamente
        tarefa_editada = self.lista_tarefas.encontrar_tarefa_por_titulo(novo_titulo)
        self.assertEqual(tarefa_editada.titulo, novo_titulo)

    def test_adicionar_e_remover_tarefa(self):
        """Testa a adição e remoção de uma tarefa"""
        titulo = "Tarefa para Remover"
        self.lista_tarefas.adicionar_tarefa(titulo)
        # Verificando se a tarefa foi adicionada
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNotNone(tarefa)
        
        # Removendo a tarefa
        self.lista_tarefas.remover_tarefa(titulo)
        tarefa_removida = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNone(tarefa_removida)
class TesteIntegracaoListaDeTarefas(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste"""
        self.lista_tarefas = ListaDeTarefas()

    def test_adicionar_e_editar_tarefa(self):
        """Testa a adição e edição de uma tarefa"""
        titulo = "Tarefa para Editar"
        self.lista_tarefas.adicionar_tarefa(titulo)
        # Verifican que a tarefa foi adicionada
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa.titulo, titulo)
        
        # Editando a tarefa
        novo_titulo = "Tarefa Editada"
        self.lista_tarefas.editar_tarefa(titulo, novo_titulo)
        # Verifica se a edição ocorreu corretamente
        tarefa_editada = self.lista_tarefas.encontrar_tarefa_por_titulo(novo_titulo)
        self.assertEqual(tarefa_editada.titulo, novo_titulo)

    def test_adicionar_e_remover_tarefa(self):
        """Testa a adição e remoção de uma tarefa"""
        titulo = "Tarefa para Remover"
        self.lista_tarefas.adicionar_tarefa(titulo)
        # Verifica se a tarefa foi adicionada
        tarefa = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNotNone(tarefa)
        
        self.lista_tarefas.remover_tarefa(titulo)
        tarefa_removida = self.lista_tarefas.encontrar_tarefa_por_titulo(titulo)
        self.assertIsNone(tarefa_removida)
