import enum
import pygame
from board import Board  # Assuming board.py contains the Board class
from engine import Engine  # Assuming engine.py contains the Engine class

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((512, 512))
        pygame.display.set_caption("Chess Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.turn = 'white'  # 'white' or 'black'
        self.human_player = 'white'  # or 'black'
        self.pc = 'black'  # Placeholder for chess engine
        self.board = Board()  # Placeholder for board representation
        self.engine = Engine(self.board)  # Placeholder for chess engine

        self.flag = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # 1. player bianco gioca
            # 2. player nero gioca
            next_move = self.get_player_move()
            if next_move: 
                # Esegui la mossa
                # print(f"Next move: {next_move}")
                # Aggiorna lo stato del gioco
                self.play_move(next_move)
                # 3. controlla se scacco matto o patta
                if self.is_gameover():
                    print("Game Over")
                    self.running = False
                self.turn = 'black' if self.turn == 'white' else 'white'

            self.screen.fill((255, 255, 255))
            self.board.draw(self.screen)  # Placeholder for drawing the board

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def get_player_move(self) -> str:
        if self.turn == self.human_player:
            # Placeholder for human move input
            return "e2e4"  # Example move
        else:
            # PC move using engine
            return self.engine.get_best_move(self.board)
        
    def play_move(self, move):
        # Placeholder for playing a move on the board
        pass

    def is_gameover(self):
        # Placeholder for game over logic
        return False

if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
