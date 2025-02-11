import pygame
import pygame.event
import pygame.image
from pygame import KEYDOWN

import ChessEngine

WIDTH = HEIGHT = 512
Dimension = 8
square_size = HEIGHT // Dimension
Max_FPS = 15
Images = {}
square_selected = ()
player_clicks = []



def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        Images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"),
                                               (square_size, square_size))


def main():
    global square_selected, square_selected, player_clicks, player_clicks
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    gs = ChessEngine.GameState()
    valid_moves = gs.get_valid_moves() or []
    move_made = False
    load_images()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.quit:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // square_size
                row = location[1] // square_size
                if square_selected == (row, col):
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (row, col)
                    player_clicks.append(square_selected)
                if 2 == len(player_clicks):
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.getchessnotation())

                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                        square_selected = ()
                        player_clicks = []
                    else:
                        player_clicks = [square_selected]

            elif e.type == KEYDOWN:
                 if e.key == pygame.K_z:
                     gs.undo_move()
                     move_made = True

        if move_made:
            valid_moves = gs.get_valid_moves() or []
            move_made = False



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
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * square_size, r * square_size, square_size, square_size))


def drawPieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(Images[piece], pygame.Rect(c * square_size, r * square_size, square_size, square_size))


if __name__ == "__main__":
    main()
