#import game_logic
#game = game_logic.Game()
#print('first' if game.random_first() == 0 else 'second')
#while True:
#    print(f'in deck {len(game_logic.game_deck)} - cards')
#    for i in game.players_list:
#        print(f'player{"1" if game.players_list.index(i) == 0 else "2"} have {i.hand}; player{"1" if game.players_list.index(i) == 0 else "2"} have {i.chests} chests')
#    print(f'player number {"1" if game.move == 0 else "2"} say card')
#    card = input('card: ')
#    game.game(card)
#    print()
#    if game.check_win():
#        print(game.check_win())
#        break

import pygame
import sys
import os
import mr_lis
import game_logic
import mr_svin
import random
import deck
import mouse_logic
import time
import threading

FPS = 60

pygame.init()
screen = pygame.display.set_mode((964, 1000))
clock = pygame.time.Clock()

background = pygame.image.load("recources/sprites/env/main.png")
start_img = pygame.image.load("recources/sprites/env/play_btn.png")
end_img = pygame.image.load("recources/sprites/env/game_over.png")
pygame.display.update()
mr_svin = mr_svin.MrSvin(screen)

#b = [deck.dict_cards[i] for i in random.choices(list(deck.dict_cards.keys()), k=13)]

f1 = pygame.font.Font(None, 36)




#cards = game_logic.get_hand(game_logic.game_deck)
#cards = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah']

def creat_new_game():
    global game, cards
    del game
    return game_logic.Game()

game = None

def new_card():
    global cards
    return game.player1.hand
cards = None
frame = 0
start_flag = True
end_flag = False
win_flag = False
def game_loop():
    global  game, cards, frame, end_flag, start_flag, win_flag
    start_flag = False
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                try:
                    game.game(mouse_logic.get_card_from_coord(*pygame.mouse.get_pos()))
                except:
                    pass
    screen.blit(background, (0, 0))
    frame += 1
    if frame == 60:
        frame = 0
    emotion = mr_svin.get_emotion()
    cards = game.player1.hand
    deck.draw_hand(cards, screen)
    deck_text = f1.render(f'В колоде осталось {len(game_logic.game_deck)}', True, (255, 255, 255))
    chest_num = f1.render(f'Вы собрали: {game.player1.chests} сундучков', True, (255, 255, 255))
    enemy_chest_num = f1.render(f'Противник собрал: {game.player2.chests} сундучков', True, (255, 255, 255))
    screen.blit(deck_text, (690, 10))
    screen.blit(chest_num, (630, 35))
    screen.blit(enemy_chest_num, (550, 60))
# 30 100 170 240 310 380 450 520 590 660 730
    #mr_svin.default_speaking_animation(frame)
    #mr_lis.get_card(screen, frame)
    #mr_svin.get_card(frame)
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    #print("Позиция курсора:", mouse_x, mouse_y)
    if game.move == 1:
        move = f1.render(f'player number {"1" if game.move == 0 else "2"} say card', True, (255, 255, 0))
        screen.blit(move, (550, 90))
        try:
            game.game(random.choice(game.player2.hand))
        except IndexError:
            win_flag = True
            end_flag = True
    if game.check_win():
        if 'svin' in game.check_win():
            win_flag = True
        end_flag = True
    deck.deck(len(game_logic.game_deck), screen)
    pygame.display.update()
once_flag = False
def start():
    with open('stat.txt') as f:
        f = [int(i.rstrip()) for i in f.readlines()]
    stats = [f1.render(f'Всего сыграно: {f[0]} партий', True, (255, 255, 255)),
             f1.render(f'Вы выиграли: {f[1]}', True, (255, 255, 255)),
             f1.render(f'Свин выиграл: {f[0] - f[1]}', True, (255, 255, 255))]
    global start_flag, game, cards
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 220 <= mouse_x <= 740 and 220 <= mouse_y <= 700:
                    start_flag = False
                    game_logic.get_deck()
                    game = creat_new_game()
                    cards = new_card()
                    with open('stat.txt', 'r') as f:
                        f11 = [int(i.rstrip()) for i in f.readlines()]
                        f11[0] += 1
                    with open('stat.txt', 'w') as f:
                        f.write(''.join([str(i) + "\n" for i in f11]))
    screen.fill((80, 125, 159))
    screen.blit(start_img, (200, 200))
    for i in range(len(stats)):
        screen.blit(stats[i], (650, 10 + 30 * i))
    pygame.display.update()

def game_over():
    global end_flag, start_flag, once_flag
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 313 <= mouse_x <= 706 and 580 <= mouse_y <= 670:
                    start_flag = True
                    end_flag = False
                    sys.exit()
    screen.fill((80, 125, 159))
    screen.blit(end_img, (200, 200))
    win = f1.render(f'{"Вы победили" if not win_flag else "Мистер Cвин победил"}', True, (255, 255, 255))
    if not win_flag and not once_flag:
        with open('stat.txt', 'r') as f:
            f11 = [int(i.rstrip()) for i in f.readlines()]
            f11[1] += 1
        with open('stat.txt', 'w') as f:
            f.write(''.join([str(i) + "\n" for i in f11]))
        once_flag = True
    screen.blit(win, (420, 400))
    pygame.display.update()


while True:
    if end_flag:
        game_over()
    elif start_flag:
        start()
    else:
        game_loop()



