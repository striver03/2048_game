import pygame
import random

import globals
import turn

pygame.init()

# inital setup
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])    # Setting dimensions
pygame.display.set_caption(title = "2048 Game by Rishabh Prasad")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf',24)


# color library
colors = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    'light text': (249, 246, 242),
    'dark text': (119, 110, 101),
    'other': (0, 0, 0),
    'bg': (187, 173, 160),
}


# variables initialization
spawn_new = True
game_over = False
init_count = 0
direction = ''
globals.initialize()
file = open('high_score.txt','r')
init_high = int(file.readline())
file.close()
high_score = init_high
board_values = [[0 for _ in range(4)] for _ in range(4)]


def draw_over():
    pygame.draw.rect(
        surface = screen,
        color = 'black',
        rect = [50,50,300,100],
        width = 0,
        border_radius = 10,
    )
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))


# move tiles based on direction
def take_turn(board,direction):
    match direction:
        case 'UP':
            return turn.take_up_turn(board = board)
        case 'DOWN':
            return turn.take_down_turn(board = board)
        case 'RIGHT':
            return turn.take_right_turn(board = board)
        case 'LEFT':
            return turn.take_left_turn(board = board)
        case default:
            return board


# spawn new piece randomly
def new_pieces(board):
    listWithZeroes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                listWithZeroes.append([i,j])

    if len(listWithZeroes) == 0:
        return board, True

    randomIdx = random.randint(a = 0, b = len(listWithZeroes)-1)    # Selecting random index from the list of tiles with no value
    [row,col] = listWithZeroes[randomIdx]

    if random.randint(1,10) == 10:  # The probabilty of spawning 4 is ~ 1/10
        board[row][col] = 4
    else:
        board[row][col] = 2

    return board, False


# draw background of the board
def draw_board():
    pygame.draw.rect(
        surface = screen,
        color = colors['bg'],
        rect = [0,0,400,400],
        border_bottom_left_radius = 10,
        border_bottom_right_radius = 10,
    )
    score_text = font.render(f'Score: {globals.score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (10,410))
    screen.blit(high_score_text, (10,450))
    pass


# draw tiles
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]

            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']

            if value < 2048:
                color =  colors[value]
            else:
                color = colors['other']

            pygame.draw.rect(
                surface = screen,
                color = color,
                rect = [j*95 + 20, i*95 + 20, 75, 75],
                border_radius = 10,
            )

            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value),True,value_color)
                text_rect = value_text.get_rect(center = (j * 95 + 57.5, i * 95 + 57.5))
                screen.blit(source = value_text, dest = text_rect)
                pygame.draw.rect(
                    surface = screen,
                    color = 'black',
                    rect = [j * 95 + 20, i * 95 + 20, 75, 75],
                    width = 2,
                    border_radius = 10,
                )


def check_possible_move(board):
    [n,m] = [len(board),len(board[0])]

    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i+1][j]:
                return False
            if board[i][j] == board[i][j+1]:
                return False
    return True


# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(color='gray')
    draw_board()
    draw_pieces(board = board_values)
    
    if spawn_new or init_count < 2:    # Initially the board is filled with 2 tiles at random locations
        board_values, is_full = new_pieces(board = board_values)
        spawn_new = False
        init_count += 1

        if is_full:
            game_over = check_possible_move(board = board_values)

    if direction != '':
        take_turn(board = board_values, direction = direction)
        direction = ''
        spawn_new = True

    if game_over:
        draw_over()
        if high_score > init_high:
            file = open('high_score.txt','w')
            file.write(f'{high_score}')
            file.close()
            init_high = high_score

    for event in pygame.event.get():    # Listening to the event
        if event.type == pygame.QUIT:   # If user clicks on X button
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

            if game_over:
                if event.key == pygame.K_RETURN:
                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                    spawn_new = True
                    init_count = 0
                    globals.score = 0
                    direction = ''
                    game_over = False

    if globals.score > high_score:
        high_score = globals.score

    pygame.display.flip()
pygame.quit()