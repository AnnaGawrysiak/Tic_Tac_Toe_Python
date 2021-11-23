import sys
import random

SIGN_CROSS = 'X'
SIGN_CIRCLE = 'O'
SIGN_EMPTY = '_'


class Player:

    def get_position(self):
        pass


class HumanPlayer(Player):
    def __init__(self, who, cross_or_circle_sign):
        self._name = who
        self._sign = cross_or_circle_sign

    # def name(self):
    #     return self._name
    #
    # def sign(self):
    #     return self._sign

    @property
    def name(self):
        # """ The name property"""
        return self._name

    # @name.setter
    # def name(self, value):
    #     self._name = value

    @property
    def sign(self):
        # """ The sign property"""
        return self._sign

    def get_position(self):  # od 0..8
        pass  # TODO:

    # @sign.setter
    # def sign(self, value):
    #     self._sign = value


class ComputerPlayer(Player):

    def get_position(self):  # od 0..8
        pass


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
        # """ The board property"""
        return self._board

    # @board.setter
    # def board(self, value):
    #     self._board = value

    # def print(self):
    #     print(self._board[0] + '|' + self._board[1] + "|" + self._board[2])
    #     print("-" + "+" + "-" + "+" + "-")
    #     print(self._board[3] + '|' + self._board[4] + "|" + self._board[5])
    #     print("-" + "+" + "-" + "+" + "-")
    #     print(self._board[6] + '|' + self._board[7] + "|" + self._board[8])
    #     print('\n')

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

    # TODO: is_line
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
            # if self.check_for_win(sign):
            #     print("Congratulations! You won!")
            #     sys.exit()
            # if self.is_full():
            #     print("The board is full. Game over.")
            #     sys.exit()
        else:
            raise OccupiedFieldError()


# b = Board()
# b.insert(0, SIGN_CROSS)
# b.insert(1, SIGN_CROSS)
# b.insert(2, SIGN_CROSS)
# assert b.check_for_win(SIGN_CROSS) == True

# SOLID

class Game:
    def __init__(self, board, player1, player2):
        self._board = board
        self._player1 = player1
        self._player2 = player2

    def run(self):
        player = self._player1
        while True:
            pos = player.get_position()  # *HumanPlayer* gdy prosimy o pozycję
            self._board.insert(pos, player.sign)
            if self._board.check_for_win(player.sign):
                return player
            elif self._board.is_full():
                return None
            if player is self._player1:
                player = self._player2
            else:
                player = self._player1


# def xsum(numbers):
#     s = 0
#     for number in numbers:
#         s += number
#     return s


def get_players():
    while True:
        choice = input("Select game mode. Press '1' for single player mode and '2' for two players mode.")
        if choice not in ('1', '2'):
            print("Not an appropriate choice.")
        else:
            break

    if choice == '1':

        return HumanPlayer(), ComputerPlayer()
    else:
        return HumanPlayer(sign=), HumanPlayer()


player1, player2 = get_players()
g = Game(player1=None, player2=None)
g.run()


class Game:

    def __init__(self):
        print("Game started")
        pass

    def _make_a_move(self, current_player, b1):
        print(f"Player {current_player.name} : tell me which field on a board should be marked .")
        field_nr = input("Enter field number (1 to 9): ")
        position = int(field_nr) - 1
        b1.insert(position, current_player.sign)
        b1.print()

    def _AI_move(self, b1):  # AI sign is Circle
        possible_moves = [key for (key, value) in b1 if value != SIGN_EMPTY]

        for i in possible_moves:
            b1[i] = SIGN_CIRCLE
            if b1.check_for_win(SIGN_CIRCLE):
                return b1.insert(i, SIGN_CIRCLE)
            b1[i] = SIGN_CROSS
            if b1.check_for_win(SIGN_CROSS):
                return b1.insert(i, SIGN_CIRCLE)

        corners_open = []

        for j in possible_moves:
            if j in [1, 3, 7, 9]:
                corners_open.append(j)

        if len(corners_open) > 0:
            return b1.insert(random.choice(corners_open), SIGN_CIRCLE)

        if 5 in possible_moves:
            return b1.insert(5, SIGN_CIRCLE)

        edges_open = []
        for i in possible_moves:
            if i in [2, 4, 6, 8]:
                edges_open.append(i)

        if len(edges_open) > 0:
            return b1.insert(random.choice(edges_open), SIGN_CIRCLE)

    def run(self):
        b1 = Board()
        print("Welcome to the Tic Tac Toe Game.")

        while True:
            choice = input("Select game mode. Press '1' for single player mode and '2' for two players mode.")
            if choice not in ('1', '2'):
                print("Not an appropriate choice.")
            else:
                break

        name1 = input("Player 1. Please enter your name: ")
        player1 = Player(name1, SIGN_CROSS)
        print(f"Player {name1}: your sign is a cross.\n")

        if choice == '2':
            name2 = input("Player 2. Please enter your name: ")
            player2 = Player(name2, SIGN_CIRCLE)
            print(f"Player {name2}: your sign is a circle.\n")
            while True:
                self._make_a_move(player1, b1)
                self._make_a_move(player2, b1)
        elif choice == '1':
            while True:
                self._make_a_move(player1, b1)
                b1.print()
                self._AI_move(b1)
                b1.print()

# def main():
#     game = Game()
#     game.run()

# main()