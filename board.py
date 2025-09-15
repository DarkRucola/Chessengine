import pygame
from pieces import Pieces

class Board:
    def __init__(self):
        # Initialize board state
        self.fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.board = self.fen_to_board(self.fen) 

        self.color_black = (125, 89, 22)
        self.color_white = (240, 189, 93)
        self.pieces = Pieces().pieces_pngs

        #"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        # rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1

        print(self.board)

    def read_fen(self, fen):
        ranks = ''
        turn = ''
        castling_rights = ''
        en_passant = '' # e.g. e3
        halfmove_clock = ''
        fullmove_number = ''

        parts = fen.split(' ') # 6 parts
        if len(parts) != 6:
            raise ValueError("Invalid FEN string")
        ranks, turn, castling_rights, en_passant, halfmove_clock, fullmove_number = parts
        ranks = ranks.split('/')
        if len(ranks) != 8:
            raise ValueError("Invalid FEN string: incorrect number of ranks")
        
    def square_to_index(self, file: str, rank: int) -> int:
        file_index = ord(file) - ord('a')  # a=0, b=1, ..., h=7
        return 21 + file_index + (8 - rank) * 10

    def fen_to_board(self, fen: str) -> list[int]:
        # inizializza board con 99
        board = [99] * 120
        piece_map = {
            'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6,
            'P':  1, 'N':  2, 'B':  3, 'R':  4, 'Q':  5, 'K':  6,
        }
        rows = fen.split()[0].split('/')
        
        for rank_index, row in enumerate(rows):
            rank = 8 - rank_index  # dalla 8a alla 1a
            file = 0
            for char in row:
                if char.isdigit():
                    file += int(char)
                    # riempi gli spazi vuoti con 0
                    for i in range(int(char)):
                        idx = self.square_to_index(chr(ord('a') + file - i), rank)
                        board[idx] = 0
                else:
                    idx = self.square_to_index(chr(ord('a') + file), rank)
                    board[idx] = piece_map[char]
                    file += 1
        return board

    def draw(self, screen):
        # Placeholder for drawing the board
        square_size = 64
        row = 0
        col = -1
        for cell in self.board:
            if cell != 99:
                if col == 7:
                    col = 0
                    row += 1
                else:
                    col += 1

                color = self.color_white if (row + col) % 2 == 0 else self.color_black
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
                pygame.draw.rect(screen, color, rect)

                piece_image = self.pieces.get(cell)
                if piece_image:
                    piece_rect = piece_image.get_rect()
                    piece_rect.topleft = ((col * square_size), (row * square_size))
                    screen.blit(piece_image, piece_rect)


if __name__ == "__main__":
    board = Board()
    b = board.fen_to_board(board.fen)
    for i in range(8):
        print(b[i*10+21:i*10+29]) # lista[start:end]

