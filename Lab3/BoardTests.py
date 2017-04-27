import unittest
import Board
import Validator

class BoardTests(unittest.TestCase):
    def test_check_players_move_is_correct(self):
        MyGame = Board.Board(4, 'x')
        x,y=2,2
        MyGame.movePlayer(x, y)
        self.assertEqual(MyGame.arrayPlayer[x][y], 1)
        self.assertEqual(MyGame.arrayGame[x][y], 1)

    def test_wchich_checks_Players_win(self):
        MyGame = Board.Board(4, 'x')
        MyGame.movePlayer(0, 0)
        MyGame.movePlayer(1, 1)
        MyGame.movePlayer(2, 2)
        MyGame.movePlayer(3, 3)
        self.assertEqual(MyGame.checkPlayersWin(),True)

    def test_wchich_checks_CPU_win(self):
        MyGame = Board.Board(4, 'x')
        MyGame.arrayCPU[0][0] = 1
        MyGame.arrayCPU[1][1] = 1
        MyGame.arrayCPU[2][2] = 1
        MyGame.arrayCPU[3][3] = 1
        self.assertEqual(MyGame.checkCPUsWin(), True)


    def test_check_if_diagonal_is_full(self):
        MyGame = Board.Board(4, 'x')
        MyGame.movePlayer(0, 0)
        MyGame.movePlayer(1, 1)
        MyGame.movePlayer(2, 2)
        MyGame.movePlayer(3, 3)
        self.assertEqual(MyGame.checkDiagonal(MyGame.arrayPlayer, True), True)

    def test_check_if_index_is_out_of_array(self):
        MyGame = Board.Board(4, 'x')
        self.assertRaises(IndexError, MyGame.movePlayer, 6, 6)


if __name__=='__main__':
    unittest.main(exit=False)