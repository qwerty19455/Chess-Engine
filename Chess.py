import pygame
import pygame.event
import pygame.image

import ChessEngine

WIDTH = HEIGHT = 512
Dimension = 8
square_size = HEIGHT // Dimension
Max_FPS = 15
Images = {}


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        Images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (square_size, square_size))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.quit:
                running = False
        clock.tick(Max_FPS)
        drawGameState(screen, gs)
        pygame.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(Dimension):
        for c in range(Dimension):
            color = colors[((r+c)%2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*square_size, r*square_size, square_size, square_size))


def drawPieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(Images[piece], pygame.Rect(c*square_size, r*square_size, square_size, square_size))

if __name__ == "__main__":
    main()