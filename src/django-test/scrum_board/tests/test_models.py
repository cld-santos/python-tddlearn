from datetime import date
from scrum_board.models import Board, Card, User
from django.test import TestCase


class ScrumBoardModelTestCase(TestCase):

    def test_must_save_a_user(self):
        user = User(name='claudio')
        user.save()

        my_saved_user = User.objects.get(name__iexact='claudio')
        self.assertEqual(my_saved_user.name, 'claudio')

    def test_must_save_a_card(self):
        user = User(name='claudio')
        user.save()

        task_to_save = Card(title='Aprendendo django',
                            description='estudando django pelo livro lightweight django',
                            owner=user,
                            created_date=date.today())
        task_to_save.save()

        my_saved_card = Card.objects.get(pk=1)
        self.assertEqual(my_saved_card.title, 'Aprendendo django')
        self.assertEqual(my_saved_card.owner.name, 'claudio')


    def test_must_save_a_board(self):
        user = User(name='claudio')
        user.save()

        task = Card(title='Aprendendo django',
                    description='estudando django pelo livro lightweight django',
                    owner=user,
                    created_date=date.today())
        task.save()

        task_b = Card(title='Aprendendo nodejs',
                      description='aguardando sugestões de fontes de estudo',
                      owner=user,
                      created_date=date.today())
        task_b.save()

        task_c = Card(title='Escrever post sobre tdd-learn',
                      description='aguardando aguardando terminar o estudo em python e django para colher informações',
                      owner=user,
                      created_date=date.today())
        task_c.save()

        board_to_save = Board()
        board_to_save.name = "Estudos"
        board_to_save.save()
        board_to_save.back_log.add(task_c)
        board_to_save.todo.add(task, task_b)
        board_to_save.save()

        my_saved_board = Board.objects.get(name__iexact='Estudos')
        self.assertEqual(my_saved_board.todo.count(), 2)
        self.assertEqual(my_saved_board.todo.all()[0].owner.name, 'claudio')
        self.assertEqual(my_saved_board.todo.first().title, 'Aprendendo django')
