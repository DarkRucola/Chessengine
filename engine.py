
from pieces import Pieces
import random
class Engine:

    def __init__(self, board):
        self.board = board  # Store the board state if needed
        self.pieces=Pieces()

    def get_best_move(self, board):
        # Placeholder for engine logic
        return "e2e4"
    def get_valid_moves(self, board: list[int], color: str) -> list[str]:
        # Placeholder for generating valid moves
        possmoves=[]
        for idx, piece_id in enumerate(board):
            if piece_id not in [99,0]:
                if color=='white' and Pieces.is_white(piece_id):
                    func=self.pieces.pieceid_tomoves.get(piece_id)
                    possmoves.append(func(board, idx))  
                elif color=='black' and Pieces.is_black(piece_id):
                    func=self.pieces.pieceid_tomoves.get(piece_id)
                    possmoves.append(func(board, idx))            

        return possmoves
    
    def get_random_move(self, board, color):
        #get a random move for the selected color
        moves= self.get_valid_moves(board, color)
        return random.choice(moves)
    