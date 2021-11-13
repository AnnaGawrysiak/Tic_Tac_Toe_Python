import sys


SIGN_CROSS = 'X'
SIGN_CIRCLE = 'O'
SIGN_EMPTY = '_'


class Player:
    def __init__(self, who, cross_or_circle_sign):
        self._name = who
        self._sign = cross_or_circle_sign

    def name(self):
        return self._name

    def sign(self):
        return self._sign


# p = Player('Jan', 'X')
# # print(p.get_name())
# print(p.name)


class OccupiedFieldError(Exception):
    pass


class PositionError(LookupError):
    pass


class Board:

    def __init__(self):
        self._board = {
            1: SIGN_EMPTY, 2: SIGN_EMPTY, 3: SIGN_EMPTY,
            4: SIGN_EMPTY, 5: SIGN_EMPTY, 6: SIGN_EMPTY,
            7: SIGN_EMPTY, 8: SIGN_EMPTY, 9: SIGN_EMPTY
        }


    def print(self):
        print(self._board[0] + '|' + self._board[1] + "|" + self._board[2])
        print("-" + "+" + "-" + "+" + "-")
        print(self._board[3] + '|' + self._board[4] + "|" + self._board[5])
        print("-" + "+" + "-" + "+" + "-")
        print(self._board[6] + '|' + self._board[7] + "|" + self._board[8])
        print('\n')

    def __str__(self):
        return '[%s | % s| %s \n -+-+- \n %s | % s| %s \n -+-+- \n %s | % s| %s \n]' % (self._board[0], self._board[1], self._board[2],
                       self._board[3], self._board[4], self._board[5],
                       self._board[6], self._board[7], self._board[8])

    def is_full(self):
        for key in self._board.keys:
            if key == SIGN_EMPTY:
                return False
            else:
                return True

    def check_for_win(self, sign):
        if self._board[0] == sign and self._board[1] == sign and self._board[2] == sign:
            return True
        elif self._board[3] == sign and self._board[4] == sign and self._board[5] == sign:
            return True
        elif self._board[6] == sign and self._board[7] == sign and self._board[8] == sign:
            return True
        elif self._board[0] == sign and self._board[3] == sign and self._board[6] == sign:
            return True
        elif self._board[1] == sign and self._board[4] == sign and self._board[7] == sign:
            return True
        elif self._board[2] == sign and self._board[5] == sign and self._board[8] == sign:
            return True
        elif self._board[0] == sign and self._board[4] == sign and self._board[8] == sign:
            return True
        elif self._board[6] == sign and self._board[4] == sign and self._board[2] == sign:
            return True
        else:
            return False

    def insert(self, position, sign):
        if position < 1 or 9 < position:
            raise PositionError()
        elif self._board[position] == SIGN_EMPTY:
            self._board[position] = sign
            if self.check_for_win(sign):
                print("Congratulations! You won!")
                sys.exit()
            if self.is_full():
               print("The board is full. Game over.")
               sys.exit()
        else:
            raise OccupiedFieldError()

class Game:

    def __init__(self):
        pass

    def _make_a_move(self, current_player):
        print(f"Player {current_player.name} : tell me which field on a board should be marked.")
        field_nr = input("Enter field number: ")
        Board.insert(field_nr, current_player.sign)
        Board.print_board()

    def run(self):
        print("Welcome to the Tic Tac Toe Game.")
        name1 = input("Player 1. Please enter your name: ")
        player1 = Player(name1, SIGN_CROSS)
        name2 = input("Player 2. Please enter your name: ")
        player2 = Player(name2, SIGN_CIRCLE)

        while True:
            self._make_a_move()

# Game().run()


# print(Board.board)

#
#
b1 = Board()
b1.insert(2, SIGN_CROSS)
print(b1)

# b1.print()


# b2 = Board()
# b2.board[2] = 'O'
# print(b2.board)


def main():
    game = Game()
    game.run()
