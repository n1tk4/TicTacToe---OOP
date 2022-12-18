from Controller import *
import unittest
from Model import *
from unittest.mock import patch
from unittest.mock import patch
import threading


class TestController(unittest.TestCase):

    def setUp(self):
        self.test_controller = Controller()
        self.test_model = Model()
        self.test_view = View(Model())

    def test_get_move(self):
        with patch('builtins.input', return_value=1):
            self.assertEqual(self.test_controller.get_move(), 1)

    def raise_keyboard_interrupt(self):
        raise KeyboardInterrupt

    def raise_value_error(self):
        raise ValueError

    def test_get_move_for_value_error(self):
        with self.assertRaises(ValueError):
            with patch.object('builtins', 'input', return_value=self.raise_value_error()):
                self.test_controller.get_move()

    def test_get_move_for_keyboard_interrupt(self):
        with self.assertRaises(KeyboardInterrupt):
            with patch.object('builtins', 'input', return_value=self.raise_keyboard_interrupt()):
                self.test_controller.get_move()

    def test_make_move(self):
        board = {1 : ' ', 2 : ' ', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' ', 8 : ' ', 9 : ' '}
        player = 'X'
        self.assertEqual(self.test_controller.make_move(board, 2, player), {1 : ' ', 2 : 'X', 3 : ' ', 4 : ' ', 5 : ' ', 6 : ' ', 7 : ' ', 8 : ' ', 9 : ' '})

    def test_player(self):
        self.test_model.player == 'X'
        assert self.test_controller.model.player == 'O'

    def test_get_winner(self):
        self.assertEqual(self.test_controller.get_winner({1: 'X', 2: 'X', 3: 'X', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: ' ', 4: 'X', 5: 'X', 6: 'X', 7: ' ', 8: ' ', 9: ' '}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: 'X', 8: 'X', 9: 'X'}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: 'X', 2: ' ', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: 'X', 3: ' ', 4: ' ', 5: 'X', 6: ' ', 7: ' ', 8: 'X', 9: ' '}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: 'X', 4: ' ', 5: ' ', 6: 'X', 7: ' ', 8: ' ', 9: 'X'}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: 'X', 2: ' ', 3: ' ', 4: ' ', 5: 'X', 6: ' ', 7: ' ', 8: ' ', 9: 'X'}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: 'X', 4: ' ', 5: 'X', 6: ' ', 7: 'X', 8: ' ', 9: ' '}), 'X')
        self.assertEqual(self.test_controller.get_winner({1: 'O', 2: 'O', 3: 'O', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: ' ', 4: 'O', 5: 'O', 6: 'O', 7: ' ', 8: ' ', 9: ' '}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: 'O', 8: 'O', 9: 'O'}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: 'O', 2: ' ', 3: ' ', 4: 'O', 5: ' ', 6: ' ', 7: 'O', 8: ' ', 9: ' '}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: 'O', 3: ' ', 4: ' ', 5: 'O', 6: ' ', 7: ' ', 8: 'O', 9: ' '}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: 'O', 4: ' ', 5: ' ', 6: 'O', 7: ' ', 8: ' ', 9: 'O'}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: 'O', 2: ' ', 3: ' ', 4: ' ', 5: 'O', 6: ' ', 7: ' ', 8: ' ', 9: 'O'}), 'O')
        self.assertEqual(self.test_controller.get_winner({1: ' ', 2: ' ', 3: 'O', 4: ' ', 5: 'O', 6: ' ', 7: 'O', 8: ' ', 9: ' '}), 'O')

    def test_is_draw(self):
        self.assertEqual(self.test_controller.is_draw({1: 'X', 2: 'O', 3: 'X', 4: 'X', 5: 'O', 6: 'X', 7: 'O', 8: 'X', 9: 'O'}), True)
        self.assertEqual(self.test_controller.is_draw({1: 'X', 2: 'X', 3: 'O', 4: 'O', 5: 'X', 6: 'X', 7: 'X', 8: 'O', 9: 'O'}), True)
        self.assertEqual(self.test_controller.is_draw({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}), False)

    def test_play(self):
        with self.assertRaises(KeyboardInterrupt):
            with patch.object('builtins.input', return_value=self.raise_keyboard_interrupt()):
                self.test_controller.play()

    def test_which_mode_choose_mode_called(self):
        with patch.object(self.test_controller.view, 'choose_mode') as mock_choose_mode:
            with patch('builtins.input', return_value='a'):
                thread = threading.Thread(target=self.test_controller.which_mode)
                thread.start()
                thread.join(1.0)

        mock_choose_mode.assert_called()


if __name__ == '__main__':
    unittest.main()
