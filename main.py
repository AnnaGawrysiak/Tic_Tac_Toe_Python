import random
from collections import namedtuple

SIGN_CROSS = 'X'
SIGN_CIRCLE = 'O'
SIGN_EMPTY = '_'


class Player:

    def get_position(self, b1):
        pass


class HumanPlayer(Player):
    def __init__(self, who, cross_or_circle_sign):
        self._name = who
        self._sign = cross_or_circle_sign

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    def get_position(self, b1):
        print(f"Player {self._name} : tell me which field on a board should be marked .")
        field_nr = input("Enter field number (1 to 9): ")
        position = int(field_nr) - 1
        while(position < 1 or position > 9):
            field_nr = input("Such field number does not exist on the board. Enter field number (1 to 9): ")
            position = int(field_nr) - 1
        while (b1.board[position] != SIGN_EMPTY):
            field_nr = input("Field has already been already occupied. Enter different field number (1 to 9): ")
            position = int(field_nr) - 1
        return position


class ComputerPlayer(Player):

    def __init__(self):
        self._name = "Computer "
        self._sign = SIGN_CIRCLE

    def get_position(self, b1):
        possible_moves = [key for (key, value) in b1.board.items() if value == SIGN_EMPTY]

        for i in possible_moves:
            b1.board[i] = SIGN_CIRCLE
            if b1.check_for_win(SIGN_CIRCLE):
                b1.board[i] = SIGN_EMPTY
                return i
            b1.board[i] = SIGN_CROSS
            if b1.check_for_win(SIGN_CROSS):
                b1.board[i] = SIGN_EMPTY
                return i
            b1.board[i] = SIGN_EMPTY

        corners_open = []

        for j in possible_moves:
            if j in [1, 3, 7, 9]:
                corners_open.append(j)

        if len(corners_open) > 0:
            return random.choice(corners_open)

        if 5 in possible_moves:
            return 5

        edges_open = []
        for i in possible_moves:
            if i in [2, 4, 6, 8]:
                edges_open.append(i)

        if len(edges_open) > 0:
            return random.choice(edges_open)

    @property
    def sign(self):
        return self._sign

    @property
    def name(self):
        return self._name

class OccupiedFieldError(Exception):
    pass


class PositionError(LookupError):
    pass


class Board:
    BOARD_SIZE = 9

    def __init__(self):
        self._board = {
            0: SIGN_EMPTY, 1: SIGN_EMPTY, 2: SIGN_EMPTY,
            3: SIGN_EMPTY, 4: SIGN_EMPTY, 5: SIGN_EMPTY,
            6: SIGN_EMPTY, 7: SIGN_EMPTY, 8: SIGN_EMPTY
        }

    @property
    def board(self):
        return self._board

    def __str__(self):
        return '[%s | % s| %s]\n[%s | % s| %s]\n[%s | % s| %s]' % (
            self._board[0], self._board[1], self._board[2],
            self._board[3], self._board[4], self._board[5],
            self._board[6], self._board[7], self._board[8]
        )

    def is_full(self):
        for value in self._board.values():
            if value == SIGN_EMPTY:
                return False
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
        if position < 0 or 9 < position:
            raise PositionError()
        elif self._board[position] == SIGN_EMPTY:
            self._board[position] = sign
        else:
            raise OccupiedFieldError()


class Game:
    def __init__(self, board, player1, player2):
        self._board = board
        self._player1 = player1
        self._player2 = player2

    def run(self):
        player = self._player1
        print(self._board)
        while True:
            pos = player.get_position(self._board)
            self._board.insert(pos, player.sign)
            print(f"The board after {player.name} move: ")
            print(self._board)
            if self._board.check_for_win(player.sign):
                print(f"Congratulations {player.name}! You are the winner.")
                return player
            elif self._board.is_full():
                print("The board is full.")
                return None
            if player is self._player1:
                player = self._player2
            else:
                player = self._player1
            print('\n')


def get_players():
    choice = input("Select game mode. Press '1' for single player mode and '2' for two players mode.")

    while choice not in ('1', '2'):
        print("Not an appropriate choice.")
        choice = input("Select game mode. Press '1' for single player mode and '2' for two players mode.")

    # import pdb; pdb.set_trace()

    if choice == '1':
        name1 = input("Tell me your name: ")
        return HumanPlayer(name1, SIGN_CROSS), ComputerPlayer()
    else:
        name1 = input("Player 1, tell me your name: ")
        name2 = input("Player 2, tell me your name: ")
        return HumanPlayer(name1, SIGN_CROSS), HumanPlayer(name2, SIGN_CIRCLE)


# Game(Board.board, player1, player2)

#b = Board()

def main():
    player1, player2 = get_players()
    board = Board()
    game = Game(board, player1, player2)
    game.run()

main()