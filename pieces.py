import enum
import pygame

class PieceIDS(enum.Enum):
    EMPTY = 0
    PAWN_W = 1
    KNIGHT_W = 2
    BISHOP_W = 3
    ROOK_W = 4
    QUEEN_W = 5
    KING_W = 6
    PAWN_B = -1
    KNIGHT_B = -2
    BISHOP_B = -3
    ROOK_B = -4
    QUEEN_B = -5
    KING_B = -6

class Pieces:
    def __init__(self):
        self.pieces_pngs = {
            PieceIDS.PAWN_W.value: "assets/white-pawn.png",
            PieceIDS.KNIGHT_W.value: "assets/white-knight.png",
            PieceIDS.BISHOP_W.value: "assets/white-bishop.png",
            PieceIDS.ROOK_W.value: "assets/white-rook.png",
            PieceIDS.QUEEN_W.value: "assets/white-queen.png",
            PieceIDS.KING_W.value: "assets/white-king.png",

            PieceIDS.PAWN_B.value: "assets/black-pawn.png",
            PieceIDS.KNIGHT_B.value: "assets/black-knight.png",
            PieceIDS.BISHOP_B.value: "assets/black-bishop.png",
            PieceIDS.ROOK_B.value: "assets/black-rook.png",
            PieceIDS.QUEEN_B.value: "assets/black-queen.png",
            PieceIDS.KING_B.value: "assets/black-king.png",
        }

        self.pieces_pngs = {k: pygame.image.load(v) for k, v in self.pieces_pngs.items()}
        # scale all images to 64x64
        self.pieces_pngs = {k: pygame.transform.scale(v, (64, 64)) for k, v in self.pieces_pngs.items()}

        assert len(self.pieces_pngs) == 12, "Error loading piece images"
        assert all(isinstance(k, int) for k in self.pieces_pngs.keys()), "Piece IDs must be integers"
        assert all(isinstance(v, pygame.Surface) for v in self.pieces_pngs.values()), "Piece images must be pygame Surfaces"

        self.pieceid_tomoves = {
            PieceIDS.PAWN_W.value: self.pawn_moves, 
            PieceIDS.KNIGHT_W.value: self.knight_moves,
            PieceIDS.BISHOP_W.value: self.bishop_moves,
            PieceIDS.ROOK_W.value: self.rook_moves,
            PieceIDS.QUEEN_W.value: lambda board, pos: self.rook_moves(board, pos) + self.bishop_moves(board, pos),
            PieceIDS.KING_W.value: self.king_moves,
            PieceIDS.PAWN_B.value: self.pawn_moves,
            PieceIDS.KNIGHT_B.value: self.knight_moves,
            PieceIDS.BISHOP_B.value: self.bishop_moves,
            PieceIDS.ROOK_B.value: self.rook_moves,
            PieceIDS.QUEEN_B.value: lambda board, pos: self.rook_moves(board, pos) + self.bishop_moves(board, pos),
            PieceIDS.KING_B.value: self.king_moves,
        }

    @staticmethod
    def is_white(piece):
        return piece in {Pieces.PAWN_W.value, Pieces.KNIGHT_W.value, Pieces.BISHOP_W.value,
                         Pieces.ROOK_W.value, Pieces.QUEEN_W.value, Pieces.KING_W.value}

    @staticmethod
    def is_black(piece):
        return piece in {Pieces.PAWN_B.value, Pieces.KNIGHT_B.value, Pieces.BISHOP_B.value,
                         Pieces.ROOK_B.value, Pieces.QUEEN_B.value, Pieces.KING_B.value}

    @staticmethod
    def rook_moves(board: list[int], position: int) -> list[int]:
        moves = []
        directions = [10, -10, 1, -1]  # up, down, right, left
        for direction in directions:
            current_pos = position
            while True:
                current_pos += direction
                if board[current_pos] == 99:  # off the board
                    break
                if board[current_pos] == 0:  # empty square
                    moves.append(current_pos)
                elif Pieces.is_white(board[position]) and Pieces.is_black(board[current_pos]):
                    moves.append(current_pos)  # capture
                    break
                elif Pieces.is_black(board[position]) and Pieces.is_white(board[current_pos]):
                    moves.append(current_pos)  # capture
                    break
                else:
                    break  # blocked by own piece
        return moves
    
    @staticmethod
    def bishop_moves(board: list[int], position: int) -> list[int]:
        moves = []
        directions = [9, -9, 11, -11]  # diagonals
        for direction in directions:
            current_pos = position
            while True:
                current_pos += direction
                if board[current_pos] == 99:  # off the board
                    break
                if board[current_pos] == 0:  # empty square
                    moves.append(current_pos)
                elif Pieces.is_white(board[position]) and Pieces.is_black(board[current_pos]):
                    moves.append(current_pos)  # capture
                    break
                elif Pieces.is_black(board[position]) and Pieces.is_white(board[current_pos]):
                    moves.append(current_pos)  # capture
                    break
                else:
                    break  # blocked by own piece
        return moves
    
    @staticmethod
    def knight_moves(board: list[int], position: int) -> list[int]:
        moves = []
        knight_jumps = [21, 19, 12, 8, -21, -19, -12, -8]
        for jump in knight_jumps:
            target_pos = position + jump
            if board[target_pos] == 99:  # off the board
                continue
            if board[target_pos] == 0:  # empty square
                moves.append(target_pos)
            elif Pieces.is_white(board[position]) and Pieces.is_black(board[target_pos]):
                moves.append(target_pos)  # capture
            elif Pieces.is_black(board[position]) and Pieces.is_white(board[target_pos]):
                moves.append(target_pos)  # capture
        return moves
    
    @staticmethod
    def king_moves(board: list[int], position: int) -> list[int]:
        moves = []
        king_steps = [10, -10, 1, -1, 9, -9, 11, -11]
        for step in king_steps:
            target_pos = position + step
            if board[target_pos] == 99:  # off the board
                continue
            if board[target_pos] == 0:  # empty square
                moves.append(target_pos)
            elif Pieces.is_white(board[position]) and Pieces.is_black(board[target_pos]):
                moves.append(target_pos)  # capture
            elif Pieces.is_black(board[position]) and Pieces.is_white(board[target_pos]):
                moves.append(target_pos)  # capture
        return moves
    
    @staticmethod
    def pawn_moves(board: list[int], position: int) -> list[int]:
        moves = []
        piece = board[position]
        if piece == Pieces.PAWN_W.value:
            # White pawn moves
            if board[position - 10] == 0:  # one square forward
                moves.append(position - 10)
                if position // 10 == 8 and board[position - 20] == 0:  # two squares from starting rank
                    moves.append(position - 20)
            # captures
            if Pieces.is_black(board[position - 9]):
                moves.append(position - 9)
            if Pieces.is_black(board[position - 11]):
                moves.append(position - 11)
        elif piece == Pieces.PAWN_B.value:
            # Black pawn moves
            if board[position + 10] == 0:  # one square forward
                moves.append(position + 10)
                if position // 10 == 3 and board[position + 20] == 0:  # two squares from starting rank
                    moves.append(position + 20)
            # captures
            if Pieces.is_white(board[position + 9]):
                moves.append(position + 9)
            if Pieces.is_white(board[position + 11]):
                moves.append(position + 11)
        return moves
    