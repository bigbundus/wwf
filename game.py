from board import fresh_board


class Game:

    def __init__(self, board_file=False):
        self.hand = []

        self.board = fresh_board
        if board_file:
            self.load_board(board_file)

    def load_board(self, board_file):
        #self.board = self.board.load_board(board_file)
        pass

    def save_board(self):
        pass

    def manually_enter_move(self):
        # A move is a position (x,y) + a direction (right or down) + a string of letters
        # not all moves are legal!

        move_input = input("Enter a move: ")
        confirm = input("Enter 'y' to confirm [" + move_input + "]: ")
        if confirm == "y":
            return move_input
        else:
            self.receive_hand_input()

    def play_move_to_board(self):
        # confirm move is legal
        # update board
        pass

    def score_move(self):
        # confirm move is legal
        # check bonus tiles
        # compute score
        pass

    def receive_hand_input(self):
        hand = input("Enter your current hand: ")
        confirm = input("Enter 'y' to confirm [" + hand + "]: ")
        if confirm == "y":
            self.hand = list(hand)
            return
        else:
            self.receive_hand_input()
