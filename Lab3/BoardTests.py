import unittest
import Board

class BoardTests(unittest.TestCase):
    def test_check_players_move_is_correct(self):
        MyGame = Board.Board(4, 'x')
        x,y=2,2
        MyGame.movePlayer(x, y)
        self.assertEqual(self.arrayPlayer[x][y], 1)
        self.assertEqual(self.arrayGame[x][y], 1)

    def test_wchich_checks_Players_win(self):
        MyGame = Board.Board(4, 'x')
        MyGame.movePlayer(0,0)
        MyGame.movePlayer(1,1)
        MyGame.movePlayer(2,2)
        MyGame.movePlayer(3,3)
        self.assertEqual(MyGame.checkPlayersWin(),True)

    def test_wchich_checks_CPU_win(self):
        MyGame = Board.Board(4, 'x')
        MyGame.movePlayer(0, 0)
        MyGame.movePlayer(1, 1)
        MyGame.movePlayer(2, 2)
        MyGame.movePlayer(3, 3)
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
        self.assertRaises(OutOfBoard, MyGame.movePlaye, 6, 6)


if __name__=='__main__':
    unittest.main(exit=False)